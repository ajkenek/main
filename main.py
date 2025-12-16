from fastapi import FastAPI, UploadFile, File
from cv import process_local_file, process_url, process_uploaded

app = FastAPI()


@app.get("/detect_local")
def detect_local(path: str):
    count = process_local_file(path)

    return {"source": "local", "file": path, "person_count": count}


@app.get("/detect_url")
def detect_url(url: str):
    count = process_url(url)

    return {"source": "url", "url": url, "person_count": count}


@app.post("/detect_upload")
async def detect_upload(file: UploadFile = File(...)):
    contents = await file.read()

    count = process_uploaded(contents)

    return {"source": "upload", "filename": file.filename,
            "person_count": count}
