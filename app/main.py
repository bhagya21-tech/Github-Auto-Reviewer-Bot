from fastapi import FastAPI 
from app.api.webhook import router as webhook_router 

app = FastAPI(title="GitHub Auto Reviewer Bot")

app.include_router(webhook_router)

@app.get("/")
def root():
    return {"message": "Reviewer bot is running 🚀"}

def add(a, b):
  return a+b
