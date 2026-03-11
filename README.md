# Sales Insight Automator

AI-powered sales analytics tool that processes CSV datasets and generates executive summaries using **Gemini AI**.

## 🚀 Features

* Upload sales CSV files
* Automatic data processing using **Pandas**
* AI-generated business insights using **Gemini AI**
* REST API built with **FastAPI**
* Containerized deployment using **Docker**
* Environment-based configuration using `.env`

## 🛠 Tech Stack

* FastAPI
* Pandas
* Google Gemini AI
* Docker
* Python

## 📂 Project Structure

```
sales-insight-automator
│
├ backend
│   ├ ai_service.py
│   ├ email_service.py
│   ├ main.py
│   └ requirements.txt
│
├ frontend
├ Dockerfile
├ docker-compose.yml
├ .gitignore
└ .env.example
```

## ▶ Run Locally

```bash
docker compose up --build
```

Open API docs:

```
http://localhost:8000/docs
```

## 📊 Example Workflow

1. Upload a CSV dataset
2. Backend processes the dataset
3. Gemini AI generates business insights
4. API returns an executive summary
