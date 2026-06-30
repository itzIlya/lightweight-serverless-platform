from __future__ import annotations

import logging
import os
import socket
import time
from urllib import error, parse, request

import redis


logger = logging.getLogger("orphan-image-cleaner")
MANIFEST_ACCEPT = ", ".join(
    [
        "application/vnd.docker.distribution.manifest.v2+json",
        "application/vnd.oci.image.manifest.v1+json",
    ]
)


def repository_and_tag(image_ref: str) -> tuple[str, str]:
    without_registry = image_ref.split("/", 1)[1]
    repository, tag = without_registry.rsplit(":", 1)
    if not repository or not tag:
        raise ValueError("Image reference must include repository and tag.")
    return repository, tag


def delete_registry_image(
    image_ref: str,
    *,
    registry_base_url: str,
    urlopen=request.urlopen,
) -> bool:
    repository, tag = repository_and_tag(image_ref)
    repository_path = "/".join(parse.quote(part, safe="") for part in repository.split("/"))
    manifest_url = (
        f"{registry_base_url.rstrip('/')}/v2/{repository_path}/manifests/"
        f"{parse.quote(tag, safe='')}"
    )
    head = request.Request(
        manifest_url,
        method="HEAD",
        headers={"Accept": MANIFEST_ACCEPT},
    )
    try:
        with urlopen(head, timeout=10) as response:
            digest = response.headers.get("Docker-Content-Digest", "")
    except error.HTTPError as exc:
        if exc.code == 404:
            return False
        raise
    if not digest:
        raise RuntimeError("Registry did not return a manifest digest.")
    delete_url = (
        f"{registry_base_url.rstrip('/')}/v2/{repository_path}/manifests/"
        f"{parse.quote(digest, safe=':')}"
    )
    delete = request.Request(delete_url, method="DELETE")
    try:
        with urlopen(delete, timeout=10):
            return True
    except error.HTTPError as exc:
        if exc.code == 404:
            return False
        raise


class OrphanImageCleaner:
    def __init__(
        self,
        redis_client,
        *,
        stream: str = "orchestrator:v2:orphan-images",
        group: str = "orphan-image-cleaners-v2",
        consumer: str | None = None,
        registry_base_url: str = "http://registry:5000",
        delete_image=delete_registry_image,
    ):
        self.redis = redis_client
        self.stream = stream
        self.group = group
        self.consumer = consumer or socket.gethostname()
        self.registry_base_url = registry_base_url
        self.delete_image = delete_image

    def ensure_group(self):
        try:
            self.redis.xgroup_create(self.stream, self.group, id="0-0", mkstream=True)
        except redis.ResponseError as exc:
            if "BUSYGROUP" not in str(exc):
                raise

    def process_once(self, *, block_ms: int = 1000, count: int = 20) -> int:
        batches = self.redis.xreadgroup(
            self.group,
            self.consumer,
            {self.stream: ">"},
            count=count,
            block=block_ms,
        )
        processed = 0
        for _, messages in batches:
            for stream_id, fields in messages:
                self.delete_image(
                    fields["image_ref"],
                    registry_base_url=self.registry_base_url,
                )
                self.redis.xack(self.stream, self.group, stream_id)
                processed += 1
        return processed


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    client = redis.Redis.from_url(
        os.getenv("REDIS_URL", "redis://localhost:6379/0"),
        decode_responses=True,
    )
    cleaner = OrphanImageCleaner(
        client,
        registry_base_url=os.getenv(
            "REGISTRY_INTERNAL_BASE_URL",
            "http://registry:5000",
        ),
    )
    cleaner.ensure_group()
    while True:
        try:
            cleaner.process_once()
        except Exception:
            logger.exception("orphan image cleanup failed")
            time.sleep(1)


if __name__ == "__main__":
    main()
