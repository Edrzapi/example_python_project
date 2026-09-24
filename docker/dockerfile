# Start from an existing Python image.
# python:3.14-slim contains a minimal Linux environment + Python 3.14.
FROM python:3.14-slim


# Set /app as the working directory inside the container.
# Following commands operate relative to this directory.
WORKDIR /app


# Copy requirements first.
# Doing this separately helps Docker cache the dependency-install layer.
COPY requirements.txt .


# Install our Python dependencies inside the image.
RUN python -m pip install --no-cache-dir -r requirements.txt


# Copy the rest of our repository into /app.
COPY . .


# Default command to execute when a container is started from this image.
CMD ["python", "src/main.py"]