# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 9090 available to the world outside this container
EXPOSE 9090

# Define environment variable
ENV NAME World

# Run fibonacci_server.py when the container launches
CMD ["python", "fibonacci_server.py"]
