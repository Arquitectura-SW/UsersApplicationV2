from dotenv import load_dotenv
import os

load_dotenv()

HOST=os.getenv('HOST')
PORT=int(os.getenv('PORT'))

MONGO_URI=os.getenv('MONGO_URI')