# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory to /app
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the dependencies
RUN npm install


# Copy the rest of the application to the container
COPY . .


# install simple http server for serving static content
RUN npm install -g http-server

# Expose the port that the application will run on
EXPOSE 8080

# Start the application
CMD ["npm", "start"]
