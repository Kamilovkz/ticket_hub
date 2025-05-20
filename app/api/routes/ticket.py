from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketRead

router = APIRouter()

@router.post("/tickets/", response_model=TicketRead)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    #TODO: Implement ticket creation logic
    new_ticket = Ticket(**ticket.dict(), user_id=1) # Assuming user_id is 1 for demo purposes

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket

@router.get("/tickets/", response_model=list[TicketRead])
async def read_tickets(db: AsyncSession = Depends(get_db)):
    results = await db.execute(select(Ticket))
    tickets = results.scalars().all()
    return tickets