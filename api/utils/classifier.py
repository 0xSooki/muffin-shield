from transformers import pipeline
from checks import *
classifier = pipeline("text-classification", model='../model')

data = extract_content(
    "https://www.bbc.com/news/world-europe-65632655")

print(classifier("TITLE: " + data["TITLE"] + " TEXT: " + data["TEXT"]))
