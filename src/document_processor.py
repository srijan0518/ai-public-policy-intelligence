from io import BytesIO
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

def read_file(uploaded_file):
    data = uploaded_file.read()
    name = uploaded_file.name.lower()

    if name.endswith(".pdf"):
        reader = PdfReader(BytesIO(data))
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    return data.decode("utf-8", errors="ignore")

def load_documents(uploaded_files):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2200,
        chunk_overlap=300,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    docs = []
    for file in uploaded_files:
        text = read_file(file)
        if not text.strip():
            continue

        for i, chunk in enumerate(splitter.split_text(text)):
            docs.append(
                Document(
                    page_content=chunk,
                    metadata={"source": file.name, "chunk": i + 1},
                )
            )
    return docs
