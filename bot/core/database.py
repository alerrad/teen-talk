from motor.motor_asyncio import AsyncIOMotorClient

from . import Config


db_client = AsyncIOMotorClient(Config.MONGO_URI)
db = db_client.get_database("teentalk")


feedback_collection = db.get_collection("feedbacks")
question_collection = db.get_collection("questions")
