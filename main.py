from fastapi import FastAPI
from routers.router import MyRuter




app = FastAPI()
app.include_router(MyRuter)