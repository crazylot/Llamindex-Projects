from fastapi import FastAPI
from core_engine import get_relevant_data, generate_response

app = FastAPI()

@app.get("/ask")
def ask(region: str, query: str):
    
    data = get_relevant_data(region)
    
    if not data:
        return {"error": "No data found"}
    
    answer = generate_response(query, data)
    
    return {
        "region": region,
        "answer": answer
    }