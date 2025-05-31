from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from core.graph import ClaimProcessingGraph

app = FastAPI()
graph = ClaimProcessingGraph()

@app.post("/process-claim")
async def process_claim(files: List[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="No files uploaded")
    result = await graph.run(files)
    return JSONResponse(content=result)
