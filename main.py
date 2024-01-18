from fastapi import FastAPI
from app.routers.v1 import items
from app.routers import auth

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(items.router)
app.include_router(auth.router)
