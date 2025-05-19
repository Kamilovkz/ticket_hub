from fastapi import APIRouter

api_router = APIRouter()

def include_router():
    from app.api.routes.ticket import router as ticket_router  # ✅ импорт внутри функции
    api_router.include_router(ticket_router, prefix="/tickets", tags=["Tickets"])
