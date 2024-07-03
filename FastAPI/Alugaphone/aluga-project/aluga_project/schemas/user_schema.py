from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    first_name: str
    middle_name: str
    cpf: int
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    first_name: str
    middle_name: str
    cpf: int
    email: EmailStr


class UsersList(BaseModel):
    users: list[UserPublic]


class Message(BaseModel):
    message: str


class UserUpdate(BaseModel):
    first_name: str | None = None
    middle_name: str | None = None
    email: str | None = None
    password: str | None = None
    active_account: str | None = None
    active_rent: str | None = None
