from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

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
    # TODO: Call prompt engineering and HuggingFace API here
    return {"email": "[Generated email will appear here]"} 