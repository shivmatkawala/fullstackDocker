# Use Node.js image
FROM node:18-alpine AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install Angular CLI globally inside the container
RUN npm install -g @angular/cli

# Install dependencies
RUN npm install

# Copy the entire Angular project
COPY . .

# Verify Angular CLI installation inside the container
RUN ng version

# Build the Angular app
RUN npm run build

# Use Nginx to serve the built Angular app
FROM nginx:alpine

# Copy the built Angular files from previous stage
COPY --from=build /app/dist /usr/share/nginx/html

# Replace default nginx.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf


# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
