from fastapi import Depends, FastAPI





from routers import items
from services import item_services

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}



app.include_router(items.router)

