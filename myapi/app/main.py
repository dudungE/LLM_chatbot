from fastapi import FastAPI
from app.schemas import QueryRequest, QueryResponse
from app.ollama_client import call_ollama_model

app = FastAPI()

@app.post("/query", response_model=QueryResponse)
def query_model(request: QueryRequest):
    response_text = call_ollama_model(request.model_name, request.prompt)
    return QueryResponse(response=response_text)
