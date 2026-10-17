# Building Stage
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Runtime Stage

FROM python:3.12-slim

WORKDIR /app

RUN useradd --create-home appuser

COPY --from=builder /install /usr/local
COPY app.py .

ENV PYTHONUNBUFFERED=1
ENV APP_NAME=Progree
ENV APP_VERSION=1.0.0

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
