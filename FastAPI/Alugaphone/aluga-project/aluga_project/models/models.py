from sqlalchemy.orm import Mapped, mapped_column, registry

table_registry = registry()


@table_registry.mapped_as_dataclass
class PhoneStock:
    __tablename__ = 'PhoneStock'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    phone_model: Mapped[str]
    brand: Mapped[str]
    chip: Mapped[bool]
    color: Mapped[str]
    price: Mapped[float]


@table_registry.mapped_as_dataclass
class UserModels:
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    first_name: Mapped[str]
    middle_name: Mapped[str]
    cpf: Mapped[int]
    active_account: Mapped[bool]
    active_rent: Mapped[bool]
    email: Mapped[str]
    password: Mapped[str]
