from pydantic import BaseModel

class TicketCreate(BaseModel):
    title: str
    description: str | None = None

class TicketRead(BaseModel):
    id: int
    title: str
    description: str
    user_id: int

    class Config:
        from_attributes = True