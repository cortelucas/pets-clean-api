import enum
from sqlalchemy import Column, String, Integer, Enum, ForeignKey
from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """Defining animal type"""

    dog: str = "dog"
    cat: str = "cat"
    fish: str = "fish"
    turtle: str = "turtle"


class Users(Base):
    """Pets Entity"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, user_id={self.user_id}]"
