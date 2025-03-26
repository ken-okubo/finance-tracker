FROM python:3.10-slim

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

RUN python manage.py collectstatic --noinput
