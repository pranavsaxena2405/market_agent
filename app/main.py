from fastapi import FastAPI
from pydantic import BaseModel
from app.agent import run_query

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/run-agent")
def handle_query(req: QueryRequest):
    return {"response": run_query(req.query)}
