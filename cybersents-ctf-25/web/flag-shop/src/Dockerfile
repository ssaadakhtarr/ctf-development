FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY views/ ./views/
COPY public/ ./public/
COPY index.js ./

EXPOSE 3000

CMD ["node", "index.js"]
