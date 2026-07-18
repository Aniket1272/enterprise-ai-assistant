from fastapi import APIRouter, File, UploadFile

from app.schemas.document_schema import UploadResponse
from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/api/v1/documents",
    tags=["Document"]
)


@router.post(
    "upload",
    response_model=UploadResponse
)
async def upload_document(
    file: UploadFile = File(...)
):
    file_name, file_path = await DocumentService.save_document(file)

    return UploadResponse(
        file_name=file_name,
        file_path=file_path,
        message="Document uploaded successfully."
    )
 