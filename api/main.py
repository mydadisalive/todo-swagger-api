from fastapi import FastAPI
from api.routers import todos

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Todo API!"}

app.include_router(todos.router)
