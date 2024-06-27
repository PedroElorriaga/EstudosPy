from typing import Optional

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    first_name: str
    middle_name: str
    cpf: int
    email: EmailStr
    password: str


class UsersList(BaseModel):
    users: list[UserSchema]


class Message(BaseModel):
    message: str


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    active_account: Optional[bool] = None
    active_rent: Optional[bool] = None
