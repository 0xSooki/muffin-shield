from fastapi import FastAPI
from lib import *
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse

class Item(BaseModel):
    url: str

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    print(test())
    return {"message": test()}

@app.post("/")
async def root(item: Item):
    print(item.url)