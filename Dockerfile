# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the index.html file to the container
COPY index.html .

# Expose port 8000 for the HTTP server
EXPOSE 8000

# Start a simple HTTP server to serve the index.html file
CMD ["python", "-m", "http.server", "8000"]
