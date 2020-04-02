#!/bin/sh

echo "Waiting for postgres..."

# listening for postgres on port 5432
while ! nc -z users-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

python manage.py run -h 0.0.0.0