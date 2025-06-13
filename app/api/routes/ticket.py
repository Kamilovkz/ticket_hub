from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.ticket import Ticket
from app.models import User
from app.schemas.ticket import TicketCreate, TicketRead

router = APIRouter()

@router.post("/tickets/", response_model=TicketRead)
async def create_ticket(
    ticket: TicketCreate, 
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
    ):
    new_ticket = Ticket(**ticket.dict(), user_id=current_user.id)
    db.add(new_ticket)
    await db.commit()
    await db.refresh(new_ticket)
    return new_ticket

@router.get("/tickets/", response_model=list[TicketRead])
async def read_tickets(db: AsyncSession = Depends(get_db)):
    results = await db.execute(select(Ticket))
    tickets = results.scalars().all()
    return tickets