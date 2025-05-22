from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserRead
from app.core.security import hash_password

router = APIRouter()

@router.post("/register", response_model=UserRead)
async def register_user(
    user_create: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).where(User.username == user_create.username))
    user = result.scalars().first()

    if user:
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    
    new_user = User(
        username=user_create.username,
        hashed_password=hash_password(user_create.password),
        email=f"{user_create.username}@example.com"
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return new_user