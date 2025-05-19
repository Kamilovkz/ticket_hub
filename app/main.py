from fastapi import FastAPI
from app.api import api_router, include_router

app = FastAPI(title="TicketHub API", version="1.0.0")

include_router()
app.include_router(api_router)