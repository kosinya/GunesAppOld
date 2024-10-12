from fastapi import APIRouter, Depends
from auth.database import User
from auth.manager import current_active_user

router = APIRouter()


@router.get('/get_current_user')
async def get_current_user(user: User = Depends(current_active_user)):
    return {"email": user.email, "name": user.name, "id": user.id}
