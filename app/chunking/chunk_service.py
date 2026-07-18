from langchain_text_splitters import RecursiveCharacterTextSplitter

class ChunkService:

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 100,
    ):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(self, text: str):

        return self.text_splitter.create_documents([text])