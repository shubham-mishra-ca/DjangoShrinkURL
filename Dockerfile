FROM python:3.11-slim

COPY . /
WORKDIR /DjangoShrinkURL

RUN pip install -r requirements.txt

RUN chmod +x /DjangoShrinkURL/shortener/migration.sh &&\
    sh /DjangoShrinkURL/shortener/migration.sh

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
