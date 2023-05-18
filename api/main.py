from fastapi import FastAPI
from utils.lib import *
from utils.soup import *
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


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
    title=extract_content(url)
    print(capsCheck(title))
    return {"message": test()}


@app.post("/")
async def root(item: Item):
    print(item.url)
