# Use a minimal Debian base image with Python
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the index.html file into the container
COPY index.html .

# Expose port 8000 for the HTTP server
EXPOSE 8000

# Command to run the HTTP server
CMD ["python", "-m", "http.server", "8000"]
