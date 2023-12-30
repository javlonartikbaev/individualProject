from datetime import datetime

from pydantic import BaseModel


# ----------------------------------- Data Base User ---------------------------------------------------
class CreateUser(BaseModel):
    login: str
    password: str
    email: str
    dateRegister: datetime = datetime.now()


class CreateUserID(CreateUser):
    idUser: int


# ---------------------------------------------------------------------------------------------

# ---------------------------- Data Base Worker -----------------------------------------------


class CreateWorker(BaseModel):
    firstName: str
    sureName: str
    dateOfBirth: datetime
    address: str
    professionCategoriesID: int
    phoneNumber: str
    user_idUser: int
    citizenship_idCitizenship: int


class CreateWorkerID(CreateWorker):
    idWorkers: int


# ---------------------------------------------------------------------------------------------


# ----------------------- DataBase Citizenship---------------------------------------------------
class CreateCitizenship(BaseModel):
    nameCitizenship: str


class CreateCitizenshipID(CreateCitizenship):
    idCitizenship: int


# -------------------------------------------------------------------------------------------


# -------------------------- create skills --------------------------------------------------
class CreateSkill(BaseModel):
    nameSkill: str


class CreateSkillID(CreateSkill):
    idSkill: int


# ----------------------------------------------------------------------------------


# ------------------------ create worker's skill ---------------------------------------
class Worker_has_skill(BaseModel):
    skill_id: int
    worker_id: int


# ----------------------------------------------------------------------------------------


# ------------------------------- Profession --------------------------------------------
class CreateProfession(BaseModel):
    nameProfession: str


class CreateProfessionID(CreateProfession):
    idProfession: int


# -------------------------------------------------------------------------------------------


class CreateCategories(BaseModel):
    nameCategories: str


class CreateCategoriesID(CreateCategories):
    idCategories: int


class ProfessionCategories(BaseModel):
    categories_id: int
    profession_id: int
