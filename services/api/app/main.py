from fastapi import FastAPI
from dotenv import load_dotenv

from app.api.routes import router

load_dotenv()

app = FastAPI(
    title="VYNX API",
    description="Local-first media utility API foundation.",
    version="0.1.0",
)
app.include_router(router)

