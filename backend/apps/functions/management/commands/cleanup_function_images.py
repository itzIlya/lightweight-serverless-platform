from django.conf import settings
from django.core.management.base import BaseCommand

from apps.functions.services import cleanup_pending_function_images


class Command(BaseCommand):
    help = "Delete registry images that are no longer referenced by active functions."

    def add_arguments(self, parser):
        parser.add_argument(
            "--registry-base-url",
            default=settings.REGISTRY_INTERNAL_BASE_URL,
        )
        parser.add_argument("--batch-size", type=int, default=100)

    def handle(self, *args, **options):
        result = cleanup_pending_function_images(
            registry_base_url=options["registry_base_url"],
            batch_size=options["batch_size"],
        )
        self.stdout.write(f"function_image_cleanup={result}")
