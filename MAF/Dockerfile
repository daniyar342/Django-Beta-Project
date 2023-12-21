FROM python:3.11
WORKDIR /usr/src/app

EXPOSE 8000

COPY requirements.txt ./

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && python manage.py collectstatic --noinput