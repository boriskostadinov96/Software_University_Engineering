from sqlalchemy import create_engine, Boolean, ForeignKey
from sqlalchemy.engine import default
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

DATABASE_URL = 'postgres+psycopg2://postgres-user:password@localhost:5432/sqlAlchemy_db'
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)


Base.metadata.create_all(engine)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    is_completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')