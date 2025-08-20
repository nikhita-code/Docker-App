FROM python:3.11-slim

WORKDIR /myapp

# Copy your Python script into the container
COPY ./api_demo.py .

RUN pip install requests

# Run the Python app
CMD ["python", "api_demo.py"]
ubuntu@ip-172-31-43-162:~/api
