from fastapi import FastAPI
from utils.checks import *
from utils.soup import *
from fastapi.middleware.cors import CORSMiddleware

from transformers import pipeline
classifier = pipeline("text-classification", model="./model")

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
async def check(url: str):
    content = extract_content(url)
    res = classifier("TITLE: " + content["TITLE"] + " TEXT: " + content["TEXT"])

    return {"validity": res}
