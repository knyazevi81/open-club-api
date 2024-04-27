from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

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
    clubs = relationship("Club", back_populates="user")

class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True)
    club_name = Column(String)
    club_adress = Column(String)
    club_id = Column(String)
    club_pm = Column(Integer , ForeignKey("users.id"))
    status = Column(String)
    pm = relationship("User", back_populates="clubs")




Base.metadata.create_all(bind=engine)
