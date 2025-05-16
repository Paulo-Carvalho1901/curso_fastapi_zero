"""
models é fazendo a modelagem do banco de dados
os modelos se preuculpa com relacionamentos do banco
"""
from datetime import datetime
from sqlalchemy.orm import registry, Mapped

# registra dados do banco
table_registry = registry()

# dataclass uma classe de dados.
# uma classe que não tem metodos, apenas atributos.
# Criando uma dataclass que representa uma tabela no banco (mapeando).
@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    # mapeando os dados
    id: Mapped[int]
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    created_at: Mapped[datetime] # saber quando user foi criado
