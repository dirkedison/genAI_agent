from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import httpx
from .prompt_engineering import build_email_prompt

# Load environment variables from .env file
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"

app = FastAPI()

# Allow frontend to access backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Email Assistant API!"}

# Placeholder for email generation endpoint
@app.post("/generate-email")
async def generate_email(request: Request):
    data = await request.json()
    user_prompt = data.get("prompt", "")
    if not user_prompt:
        return {"error": "Prompt is required."}

    # Build the LLM prompt
    llm_prompt = build_email_prompt(user_prompt)

    # Call HuggingFace Inference API
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    payload = {"inputs": llm_prompt}
    async with httpx.AsyncClient() as client:
        response = await client.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
        if response.status_code != 200:
            return {"error": f"HuggingFace API error: {response.text}"}
        result = response.json()
        # The output format may vary by model; handle accordingly
        generated_email = result[0]["generated_text"] if isinstance(result, list) and "generated_text" in result[0] else result
    return {"email": generated_email} 