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
