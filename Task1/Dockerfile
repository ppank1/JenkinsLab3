# Use Python 3.6 or later as a base image
FROM python:3.9-slim

# Copy contents into image
COPY . /app
WORKDIR /app

# Install pip dependencies from requirements
RUN pip install -r requirements.txt

# Set your name environment variable
ENV prem="friend"

# Expose the correct port
EXPOSE 5500

# Create an entrypoint
ENTRYPOINT ["python", "app.py"]
