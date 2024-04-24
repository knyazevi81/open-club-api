from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./app_sql.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

class Base(DeclarativeBase): pass

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_status = Column(Integer,)



Base.metadata.create_all(bind=engine)
