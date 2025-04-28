from fastapi import FastAPI
from pydantic import BaseModel
from src.utils import get_answer

app = FastAPI()


class Question(BaseModel):
    question: str
    pdf: str


@app.get("/")
def root():
    return {"status": "Backend server is operational"}


@app.post("/ask")
def ask_question(question: Question):
    ans = get_answer(pdf_string=question.pdf, question=question.question)
    return ans
