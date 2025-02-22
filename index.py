from fastapi import FastAPI
from routes.user import user 
app = FastAPI()
app.include_router(user)
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI MongoDB Project!"}
