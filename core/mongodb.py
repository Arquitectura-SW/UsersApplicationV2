
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from core.config.config import MONGO_URI

uri = MONGO_URI

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.BancoLosAlpes

clientes = db['clientes']