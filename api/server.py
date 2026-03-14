from fastapi import FastAPI
from agents.student_agent import student_agent

app = FastAPI()

@app.post("/ask")

async def ask_agent(question: str):

    response = student_agent.run(question)

    return {"response": response}