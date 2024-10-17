from datetime import date

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    name: str
    date_of_birth: date


class UserCreate(schemas.BaseUserCreate):
    name: str
    date_of_birth: date


class UserUpdate(schemas.BaseUserUpdate):
    name: str
    date_of_birth: date
