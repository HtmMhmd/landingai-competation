from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import List
from crew.crew import run_crew
import tempfile
import shutil
import os

app = FastAPI(title="FinDoc Insight API")

@app.get("/")
async def root():
    return {"message": "FinDoc Insight API - Financial Document Analysis", "version": "1.0.0"}

@app.post("/analyze")
async def analyze(
    files: List[UploadFile] = File(...),
    analysis_type: str = Form(...)
):
    temp_dir = tempfile.mkdtemp()
    file_paths = []

    try:
        for file in files:
            file_location = os.path.join(temp_dir, file.filename)
            with open(file_location, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            file_paths.append(file_location)

        report = await run_crew(file_paths, analysis_type)

        return JSONResponse(content=report)

    finally:
        shutil.rmtree(temp_dir)

@app.get("/health")
async def health():
    return {"status": "healthy"}
