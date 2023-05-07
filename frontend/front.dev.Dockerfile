FROM node:lts-alpine
WORKDIR /app
ADD . ./
CMD npm install && npm run serve
EXPOSE 8080