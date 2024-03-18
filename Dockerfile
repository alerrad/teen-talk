FROM python:3.12-alpine

WORKDIR /bot

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG BOT_TOKEN=""
ARG MONGO_URI=""
ARG OPENAI_KEY=""

ENV BOT_TOKEN=${BOT_TOKEN}
ENV MONGO_URI=${MONGO_URI}
ENV OPENAI_KEY=${OPENAI_KEY}

CMD ["python", "main.py"]