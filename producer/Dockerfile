# Dockerfile, Image, Container
FROM python:3.14.6

WORKDIR /app/producer
# building from project root so root sees "producer"
COPY . /app/producer/
# install dependencies first since Docker caches
RUN pip install --no-cache-dir .

CMD ["python", "-m", "producer.generator"]