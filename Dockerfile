FROM python:3.12-alpine

WORKDIR /bot

COPY . /bot

RUN pip install --no-cache-dir -r requirements.txt

ENV BOT_TOKEN=<bot_token>

CMD ["python", "main.py"]