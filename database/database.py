import datetime

from sqlalchemy import (
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    create_engine,
    Column,
    TIMESTAMP,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
import pymysql


Base = declarative_base()
# ---------------------------- DataBase User -----------------------------------------------


class Users(Base):
    __tablename__ = "users"

    idUser = Column(Integer, autoincrement=True, primary_key=True)
    login = Column(String(50), unique=True)
    password = Column(String(45))
    email = Column(String(45), unique=True)
    dateRegister = Column(TIMESTAMP, default=datetime.datetime.utcnow())
    workers = relationship("Workers", back_populates="users")


# ---------------------------------------------------------------------------------------------

# -------------------------------  DataBase Worker --------------------------------------------


class Workers(Base):
    __tablename__ = "workers"

    idWorkers = Column(Integer, primary_key=True, autoincrement=True)
    firstName = Column(String(45))
    sureName = Column(String(45))
    dateOfBirth = Column(DateTime)
    address = Column(String(45))
    phoneNumber = Column(String(45))
    user_idUser = Column(Integer, ForeignKey("users.idUser"))
    users = relationship(
        "Users",
        back_populates="workers",
        primaryjoin="Workers.user_idUser == Users.idUser",
    )

    citizenship_idCitizenship = Column(
        Integer, ForeignKey("citizenships.idCitizenship")
    )
    citizenships = relationship(
        "Citizenships",
        back_populates="workers",
        primaryjoin="citizenship_idCitizenship == Citizenship.idCitizenship",
    )


# -----------------------------------------------------------------------------------------------


# --------------------------------- DataBase Citizenship -----------------------------------------
class Citizenship(Base):
    __tablename__ = "citizenships"

    idCitizenship = Column(Integer, primary_key=True, autoincrement=True)
    nameCitizenship = Column(String(45), unique=True, nullable=False)
    workers = relationship("Workers", back_populates="citizenships")
