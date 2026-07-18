from pathlib import Path

from fastapi import UploadFile

from app.utils.file_utils import (
    UPLOAD_DIRECTORY,
    generate_file_name
)


class DocumentService:

    @staticmethod
    async def save_document(file: UploadFile):

        unique_name = generate_file_name(file.filename)

        destination = UPLOAD_DIRECTORY / unique_name

        contents = await file.read()

        destination.write_bytes(contents)

        return unique_name, str(destination)