# Dockerfile: Use an official Python runtime as a parent image
FROM python:3.6-slim
# Set the working directory to /app
WORKDIR /model-server:default
# Copy the current directory contents into the container at /app
ADD . /model-server:default
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements-server.txt
# Make port 80 available to the world outside this container
# Define environment variable
# ENV NAME World
# Run app.py when the container launches
CMD ["python", "main-server.py"]
