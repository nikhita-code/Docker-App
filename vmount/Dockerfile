# Use lightweight Python base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /myapp

# Copy your Python program into container
COPY ./myapp.py .

# Copy server.txt into container
COPY ./server.txt .

# Run the Python program when the container starts
CMD ["python", "myapp.py"]
