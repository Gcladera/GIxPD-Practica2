# Dockerfile: Use an official Python runtime as a parent image
FROM python:3.8
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
ADD requirements-train.txt .
ADD main-train.py .
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements-train.txt
# Make port 80 available to the world outside this container
# Define environment variable
# ENV NAME World
# Run app.py when the container launches
CMD ["python3", "main-train.py"]
