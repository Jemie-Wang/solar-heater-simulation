# Use an official Python runtime as a parent image
FROM python:3.9

RUN apt-get update && \
      apt-get -y install sudo

RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 

# Set the environment variable to indicate that Flask will be run in production mode
ENV FLASK_ENV=production

ADD . .

RUN ls

EXPOSE 8000

# Set the command to run the Flask application
CMD ["python", "main.py"]
