FROM node:14.14.0-alpine

COPY package.json yarn.lock /app/

WORKDIR /app

RUN yarn install

COPY . /app

CMD ["yarn", "serve"]
