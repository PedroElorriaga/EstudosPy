from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from aluga_project.database.database import create_session
from aluga_project.models.models import PhoneStock
from aluga_project.schemas.schema import PhonesList

Session = Annotated[Session, Depends(create_session)]

router = APIRouter(prefix='/phones', tags=['phones'])


@router.get('/', status_code=200, response_model=PhonesList)
def phone_get(session: Session, skip: int = 0, limit: int = 100):

    phones_list_from_db = session.scalars(
        select(PhoneStock).offset(skip).limit(limit)
    ).all()

    return {'phones': phones_list_from_db}
