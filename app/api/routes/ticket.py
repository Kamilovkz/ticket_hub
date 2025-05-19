from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketRead

router = APIRouter()

@router.post("/tickets/", response_model=TicketRead)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    new_ticket = Ticket(**ticket.dict(), user_id=1) # Assuming user_id is 1 for demo purposes

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket
