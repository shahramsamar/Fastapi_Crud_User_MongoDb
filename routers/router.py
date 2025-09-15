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
   
@MyRuter.put("/update_user/{username}")
async  def update_user(username: str, updated_user: User):
    result = users_table.update_one(
        {"username": username},
        {"$set": updated_user.dict()}
    )   
    if result.modified_count:
        return {"message" : "user updated successfully"}
    return {"message" : "User not found"}