from pydantic import BaseModel


class PhoneSchema(BaseModel):
    phone_model: str
    brand: str
    chip: bool
    color: str
    price: float


class PhonesList(BaseModel):
    phones: list[PhoneSchema]


class Message(BaseModel):
    message: str
