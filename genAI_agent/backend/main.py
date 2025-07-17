from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import httpx
from prompt_engineering import build_email_prompt
from pydantic import BaseModel
from huggingface_hub import InferenceClient
import re

# Load environment variables from .env file
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/HuggingFaceTB/SmolLM3-3B"

app = FastAPI()

# Allow frontend to access backend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = InferenceClient(
    provider="hf-inference",
    api_key=os.environ["HUGGINGFACE_API_KEY"],
)

class EmailPromptRequest(BaseModel):
    prompt: str

def remove_think_blocks(text: str) -> str:
    # Remove all <think>...</think> blocks (including multiline)
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Email Assistant API!"}

# Placeholder for email generation endpoint
@app.post("/generate-email")
async def generate_email(request: EmailPromptRequest):
    user_prompt = request.prompt
    if not user_prompt:
        return {"error": "Prompt is required."}

    llm_prompt = build_email_prompt(user_prompt)

    # Use the new chat completion API
    completion = client.chat.completions.create(
        model="HuggingFaceTB/SmolLM3-3B",
        messages=[
            {
                "role": "user",
                "content": llm_prompt
            }
        ],
    )
    generated_email = completion.choices[0].message.content
    cleaned_email = remove_think_blocks(generated_email)
    return {"email": cleaned_email} 