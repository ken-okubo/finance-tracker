#!/bin/sh

echo "Waiting for PostgreSQL to be ready..."
python manage.py wait_for_db

echo "PostgreSQL is up! Starting Django..."
python manage.py runserver 0.0.0.0:8000
