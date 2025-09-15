from fastapi import APIRouter
from models.model import User
from configurations.database import users_table


MyRuter = APIRouter()


@MyRuter.post("/add_user")
async def add_user(user: User):
    user_data = user.dict()
    users_table.insert_one(user_data)
    return {"messsage": "User added successfully"}

@MyRuter.get("/usres")
async def get_users():
       users = list(users_table.find(
           {},{"_id":0})) 
       return {"users":users}