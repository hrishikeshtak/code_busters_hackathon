FROM node:latest as build

# Set the working directory
ENV PROJECT_DIR=/usr/local/app
RUN mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR

# Add the source code to app
COPY ./src $PROJECT_DIR/src
COPY ./package.json $PROJECT_DIR/
COPY ./angular.json $PROJECT_DIR/

# Install all the dependencies
RUN npm install

# Generate the build of the application
RUN npm run build


# Stage 2: Serve app with nginx server

# Use official nginx image as the base image
FROM nginx:latest

# Copy the build output to replace the default nginx contents.
COPY --from=build /usr/local/app/dist/code_busters_ui /usr/share/nginx/html

# Expose port 80
EXPOSE 80

CMD ["/bin/bash"]

