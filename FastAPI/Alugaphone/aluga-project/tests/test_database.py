from sqlalchemy import select

from aluga_project.models.models import PhoneStock


def test_add_phone_in_stock(session):
    new_phone = PhoneStock(
        phone_model='Iphone 14 PRO MAX',
        brand='Apple',
        chip=True,
        color='Black',
        price=4950.00,
    )

    session.add(new_phone)
    session.commit()

    phone = session.scalar(select(PhoneStock).where(PhoneStock.id == 1))

    assert phone.phone_model == 'Iphone 14 PRO MAX'
