from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Column, Integer, String

from database import Base


class User(SQLAlchemyBaseUserTable[id], Base):
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(), nullable=False)
    date_of_birth = Column(String(), nullable=False)
