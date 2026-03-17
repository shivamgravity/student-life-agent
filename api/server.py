from fastapi import FastAPI
from pydantic import BaseModel
from agents.student_agent import student_agent

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
async def ask_agent(query: Query):

    response = student_agent(query.question)

    return {"response": response}