from pathlib import Path
import uuid


UPLOAD_DIRECTORY = Path("uploads")

UPLOAD_DIRECTORY.mkdir(exist_ok=True)


def generate_file_name(filename: str):

    extension = Path(filename).suffix

    unique_name = f"{uuid.uuid4()}{extension}"

    return unique_name