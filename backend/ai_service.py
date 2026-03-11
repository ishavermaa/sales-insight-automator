import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")


def generate_summary(df):

    data_text = df.to_string()

    prompt = f"""
    Analyze this sales dataset and generate a professional summary
    for executive leadership.

    Dataset:
    {data_text}

    Include:
    - total revenue
    - best performing region
    - best selling product category
    - key insights
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:
        return "AI summary could not be generated due to API quota limits, but the dataset was processed successfully."