from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Knowledge Assistant",
    description="RAG-powered AI backend service",
    version="1.0.0",
)

@app.get("/")
def health_check():
    return {
        "status": "UP",
        "application": "Enterprise AI Knowledge Assistant"
    }