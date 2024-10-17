from fastapi_users import FastAPIUsers
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.auth import auth_backend
from database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from auth.router import router as user_router

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI()
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(user_router, prefix="/user", tags=["user"])

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type", "Authorization", "Access-Control-Request-Headers", "Access-Control-Allow-Headers"],
)
