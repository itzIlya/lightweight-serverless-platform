ARG NODE_IMAGE=mirror-docker.runflare.com/library/node:22-alpine
FROM ${NODE_IMAGE}

WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .

EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
