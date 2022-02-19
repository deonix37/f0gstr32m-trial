FROM python:3.10.2
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update \
    && apt-get install -y gdal-bin
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY app /app/
