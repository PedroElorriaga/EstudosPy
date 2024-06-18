from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class PhoneStock(Base):
    __tablename__ = 'PhoneStock'

    id: Mapped[int] = mapped_column(primary_key=True)
    phone_model: Mapped[str]
    brand: Mapped[str]
    chip: Mapped[bool]
    color: Mapped[str]
    price: Mapped[float]


class UserModels(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    middle_name: Mapped[str]
    cpf: Mapped[int]
    active_account: Mapped[bool]
    active_rent: Mapped[bool]
