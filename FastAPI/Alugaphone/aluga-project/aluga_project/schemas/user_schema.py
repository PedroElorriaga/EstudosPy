from pydantic import BaseModel


class UserSchema(BaseModel):
    first_name: str
    middle_name: str
    cpf: int
    active_account: bool
    active_rent: bool


class UsersList(BaseModel):
    users: list[UserSchema]


class Message(BaseModel):
    message: str
