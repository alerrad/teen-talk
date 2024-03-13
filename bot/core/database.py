from motor.motor_asyncio import AsyncIOMotorClient

from . import Config


db_client = AsyncIOMotorClient(Config.MONGO_URI)
db = db_client.get_database("teentalk")

# get feedbacks collection
feedback_collection = db.get_collection("feedbacks")
