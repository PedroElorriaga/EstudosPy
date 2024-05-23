from pydantic import BaseModel


class PhonesStocks(BaseModel):
    phone_model: str
    brand: str
    chip: bool
    color: str
    price: float


class PhonesList(BaseModel):
    phones: list[PhonesStocks]
