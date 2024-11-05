# Use the official Nginx image from Docker Hub
FROM nginx:alpine

# Copy the index.html file to the Nginx HTML directory
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 for the Nginx server
EXPOSE 80
