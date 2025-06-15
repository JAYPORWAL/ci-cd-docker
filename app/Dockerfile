# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install pygame dependencies
RUN apt-get update && \
    apt-get install -y python3-dev libsdl-image1.2-dev libsdl-mixer1.2-dev \
    libsdl-ttf2.0-dev libsmpeg-dev libsdl1.2-dev libjpeg-dev libpng-dev \
    libportmidi-dev ffmpeg && \
    apt-get clean

# Copy app
COPY app.py .

# Install Python dependencies
RUN pip install pygame

# Set default command to run the game
CMD ["python", "app.py"]
