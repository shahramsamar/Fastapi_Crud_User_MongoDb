from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



uri = "mongodb://localhost:27017/?directConnection=true"

client = MongoClient(uri, server_api=ServerApi("1"))


try:
    client.admin.command("ping")
    print("Pinged your deployment.You successfilly connected to MongoDb!!!!!")

except Exception as e:
    print(e)

db = client["user"]
users_table = db['users']    
    