FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY App ./App
COPY alembic ./alembic
COPY alembic.ini .

CMD ["sh", "-c", "alembic upgrade head && uvicorn App.main:app --host 0.0.0.0 --port ${PORT:-8000}"]