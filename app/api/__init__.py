from fastapi import APIRouter

api_router = APIRouter()

def include_router():
    from app.api.routes.ticket import router as ticket_router  # ✅ импорт внутри функции
    from app.api.routes.auth import router as auth_router
    api_router.include_router(ticket_router, prefix="/tickets", tags=["Tickets"])
    api_router.include_router(auth_router, prefix="/auth", tags=['Auth'])