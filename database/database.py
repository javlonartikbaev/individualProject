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
    Table,
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
    workers = relationship("Workers", back_populates="users", uselist=False)


# ---------------------------------------------------------------------------------------------
#
# Worker_has_skill = Table(
#     "workers_has_skills",
#     Base.metadata,
#     Column("idWorkerHasSkill", Integer, primary_key=True, autoincrement=True),
#     Column("skill_id", Integer, ForeignKey("skills.idSkill")),
#     Column("worker_id", Integer, ForeignKey("workers.idWorkers")),
# )


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
        "Citizenship",
        back_populates="workers",
        primaryjoin="Workers.citizenship_idCitizenship == Citizenship.idCitizenship",
    )
    skills = relationship(
        "Skill", secondary="workers_and_skills", back_populates="workers"
    )
    professionCategoriesID = Column(
        Integer, ForeignKey("professionCategories.ProfessionCategories_id")
    )
    professionCategories = relationship(
        "ProfessionCategoriesORM", back_populates="workersProfession"
    )


# -----------------------------------------------------------------------------------------------


# --------------------------------- DataBase Citizenship -----------------------------------------
class Citizenship(Base):
    __tablename__ = "citizenships"

    idCitizenship = Column(Integer, primary_key=True, autoincrement=True)
    nameCitizenship = Column(String(45), unique=True, nullable=False)
    workers = relationship("Workers", back_populates="citizenships")


# -----------------------------------------------------------------------------------------------
# --------------------------------- DataBase Citizenship -----------------------------------------
class Skill(Base):
    __tablename__ = "skills"

    idSkill = Column(Integer, primary_key=True, autoincrement=True)
    nameSkill = Column(String(45), unique=True, nullable=False)
    workers = relationship(
        "Workers", secondary="workers_and_skills", back_populates="skills"
    )


# ---------------------------------------------------------------------------------------------

# -------------------------------- Worker has skill ------------------------------------------


class WorkerAndSkill(Base):
    __tablename__ = "workers_and_skills"

    worker_id = Column(Integer, ForeignKey("workers.idWorkers"), primary_key=True)
    skill_id = Column(Integer, ForeignKey("skills.idSkill"), primary_key=True)


# --------------------------- Profession -------------------------------------------------------


class ProfessionOrm(Base):
    __tablename__ = "professions"

    idProfession = Column(Integer, primary_key=True, autoincrement=True)
    nameProfession = Column(String(50))
    categories = relationship(
        "CategorisOrm", secondary="professionCategories", back_populates="proffesion"
    )


class CategorisOrm(Base):
    __tablename__ = "categories"

    idCategories = Column(Integer, primary_key=True, autoincrement=True)
    nameCategories = Column(String(50))
    proffesion = relationship(
        "ProfessionOrm",
        secondary="professionCategories",
        back_populates="categories",
    )


class ProfessionCategoriesORM(Base):
    __tablename__ = "professionCategories"

    ProfessionCategories_id = Column(Integer, primary_key=True, autoincrement=True)
    profession_id = Column(
        Integer, ForeignKey("professions.idProfession"), primary_key=True
    )
    categories_id = Column(
        Integer, ForeignKey("categories.idCategories"), primary_key=True
    )
    workersProfession = relationship("Workers", back_populates="professionCategories")


# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------- University and Education ---------------------------------------------------------


