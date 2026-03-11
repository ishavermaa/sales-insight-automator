from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io
from ai_service import generate_summary

app = FastAPI(title="Sales Insight Automator API")

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow React localhost
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    email: str = Form(...)
):

    contents = await file.read()

    try:

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

    except Exception as e:
        return {"error": str(e)}