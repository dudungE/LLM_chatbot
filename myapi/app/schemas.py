from pydantic import BaseModel

class QueryRequest(BaseModel):
    model_name: str
    prompt: str

class QueryResponse(BaseModel):
    response: str
