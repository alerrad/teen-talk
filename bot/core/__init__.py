from redis.asyncio import Redis
from .config import Config
from .bot import bot, dp
from .logger import logger
from .database import feedback_collection

redis_client = Redis(host="redis", port=6379, db=0)