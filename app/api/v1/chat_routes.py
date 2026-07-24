from fastapi import APIRouter

from app.schemas.chat_schema import ChatRequest
from app.services.rag_service import RAGService

router = APIRouter(prefix="/chat", tags=["chat"])

rag = RAGService()


@router.post("/")
def chat(request: ChatRequest):

    return {
        "answer": rag.ask(request.question)
    }