from fastapi import FastAPI, UploadFile, File, Form
import pandas as pd
import io
from ai_service import generate_summary

app = FastAPI(title="Sales Insight Automator API")

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    email: str = Form(...)
):

    contents = await file.read()

    if file.filename.endswith(".csv"):
        df = pd.read_csv(io.BytesIO(contents))

    elif file.filename.endswith(".xlsx"):
        df = pd.read_excel(io.BytesIO(contents))

    else:
        return {"error": "Only CSV or XLSX files allowed"}

    summary = generate_summary(df)

    return {
        "message": "AI summary generated successfully",
        "summary": summary,
        "email": email
    }