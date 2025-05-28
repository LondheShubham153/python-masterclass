FROM python:3.12-slim-bookworm
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y gcc python3-dev && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN useradd -m appuser
RUN chown appuser /app
USER appuser
CMD ["python3","app.py"]
