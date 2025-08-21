FROM python:3.11-slim

WORKDIR /myapp

# Copy your Python script into the container
COPY ./sql_demo.py .


RUN pip install pymysql
RUN pip install cryptography 

# Run the Python app
CMD ["python", "sql_demo.py"]
