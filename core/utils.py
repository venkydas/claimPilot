import io
import os
import tempfile
import inspect



from PyPDF2 import PdfReader
from llama_parse import LlamaParse


async def pdf_to_text(file) -> str:
    # Read file-like object asynchronously and wrap in BytesIO
    contents = file.read()
    file_stream = io.BytesIO(contents)
    reader = PdfReader(file_stream)

    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()

async def get_markdown(file, filename: str = None) -> str:
    parser = LlamaParse(
        api_key=os.getenv("LLAMA_CLOUD_API_KEY"),
        result_type="markdown",
        verbose=False,
    )

    if isinstance(file, (str, os.PathLike)):
        file_name = filename or os.path.basename(str(file))
        docs = parser.load_data(str(file), extra_info={"file_name": file_name})

    else:
        # Async read (handle FastAPI's UploadFile and similar)

        if inspect.iscoroutinefunction(file.read):
            file_bytes = await file.read()
        else:
            file_bytes = file.read()
   

        file_name = (
            getattr(file, "filename", None)
            or getattr(file, "name", None)
            or filename
            or "uploaded.pdf"
        )

        # Create the temp file with delete=False
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            tmp.write(file_bytes)
            tmp_path = tmp.name

        try:
            docs = parser.load_data(tmp_path, extra_info={"file_name": file_name})
        finally:
            # Make sure to delete the temp file after parsing
            os.remove(tmp_path)

    markdown_blocks = [doc.text for doc in docs]
    return "\n".join(markdown_blocks).strip()

