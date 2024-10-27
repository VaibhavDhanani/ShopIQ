# Use Python slim base image for smaller size
FROM python:3.12-slim

# Prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTRACE=1 \
    PYTHONUNBUFFERED=1 \
    # Disable pip's cache dir
    PIP_NO_CACHE_DIR=1 \
    # Don't check for pip updates
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set work directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Set build arguments with defaults
ARG DJANGO_SECRET_KEY="default-secret-key-change-in-production"
ARG DJANGO_DEBUG=0
ARG PROJ_NAME="shopiq"

# Set environment variables
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY} \
    DJANGO_DEBUG=${DJANGO_DEBUG}

# Collect static files
RUN python manage.py collectstatic --noinput

# Create startup script
RUN echo '#!/bin/bash\n\
PORT="${PORT:-8000}"\n\
python manage.py migrate --no-input\n\
gunicorn '"${PROJ_NAME}"'.wsgi:application --bind "0.0.0.0:$PORT"' > /code/start.sh && \
    chmod +x /code/start.sh

# Expose port
EXPOSE 8000

# Run startup script
CMD ["/code/start.sh"]