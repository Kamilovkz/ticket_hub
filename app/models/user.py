from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)  
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(32), nullable=False)

    tickets = relationship("Ticket", back_populates="user")



    