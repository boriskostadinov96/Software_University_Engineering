from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)


class Chef(Base):
    __tablename__ = "chefs"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    recipes = relationship(
        "Recipe",
        back_populates="chef"
    )
