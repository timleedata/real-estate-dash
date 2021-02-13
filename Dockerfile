# Pull official base image
FROM python:3.6.12-slim

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Apply migrations
RUN python manage.py migrate --noinput

# run gunicorn
CMD gunicorn tldata_web.wsgi:application --bind 0.0.0.0:$PORT
