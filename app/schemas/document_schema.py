from pydantic import BaseModel


class UploadResponse(BaseModel):
    file_name: str
    file_path: str
    message: str