from sqlalchemy import select

from fast_zero.models import Usuario


def test_criar_usuario(session):
    novo_usuario = Usuario(
        username='Pedro', email='pedrinhoGamer@sccp.com', password='Sccp1910'
    )
    session.add(novo_usuario)
    session.commit()

    usuario = session.scalar(
        select(Usuario).where(Usuario.username == 'Pedro')
    )

    assert usuario.username == 'Pedro'
