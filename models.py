"""
models é 

"""

from sqlalchemy.orm import registry


table_registry = registry()

# Uma classe de dados 
# uma classe que não tem metodos, apenas atributos
# Criando uma dataclass que representa uma tabela no banco (mapeando)
@table_registry.mapped_as_dataclass
class User:
    ...

    id: int
    username: str
    password: str
    email: str