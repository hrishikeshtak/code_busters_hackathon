FROM node:latest as build

#FROM node:16-alpine AS build
ENV PROJECT_DIR=/app/code_busters
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR

#COPY package*.json ./
COPY . $PROJECT_DIR/
RUN npm install
#COPY . .
RUN npm run build
EXPOSE 8095
CMD ["npm", "start"]