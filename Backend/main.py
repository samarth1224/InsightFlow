from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from summarize import Summarize
import os


class TextData(BaseModel):
        text: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("GEMINI_API_KEY")
@app.post("/summarize/text")
async def summarize_text(type: str, text: TextData):

        summary = Summarize(api_key=API_KEY)
        summarized_text =  await summary.summarize_text(text=text.text,type=type)
        return {"summary" : summarized_text}



@app.get('/')
async def root():
    return "Hellow Wolrds"


