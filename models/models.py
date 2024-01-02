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


# ---------------------------------------- Profession and Categories -------------------------
class CreateCategories(BaseModel):
    nameCategories: str


class CreateCategoriesID(CreateCategories):
    idCategories: int


class ProfessionCategories(BaseModel):
    categories_id: int
    profession_id: int


class ProfessionCategoriesID(ProfessionCategories):
    ProfessionCategories_id: int


# ----------------------------------------------------------------------------------------------------------------


# ------------------------------------ University and Education --------------------------------------------------
class CreateUniversity(BaseModel):
    nameUniversity: str
    nameFaculty: str
    specialization: str
    dateOfStart: datetime
    dateOfEnd: datetime


class CreateUniversityID(CreateUniversity):
    idUniversity: int


# -----------------------------------------------------------
class CreateEducation(BaseModel):
    nameEducation: str


class CreateEducationID(CreateEducation):
    idEducation: int


# -----------------------------------------------------------


class CreateUniversityEducation(BaseModel):
    university_id: int
    education_id: int


class CreateUniversityEducationID(CreateUniversityEducation):
    idUniversityEducation: int


class CreateWorkerUniversityEducation(BaseModel):
    worker_idWorker: int
    education_university: int


class CreateWorkerUniversityEducationID(CreateWorkerUniversityEducation):
    id: int


# ---------------------------------------------------------------------------------------------------------------------

# ------------------------------ Experience ----------------------------------------------------------------------------


class CreateExperience(BaseModel):
    nameCompany: str
    dateOfStart: datetime
    dateOfEnd: datetime


class CreateExperienceID(CreateExperience):
    idExperience: int


# ------------------------------------------------------
class CreateWorkerExperience(BaseModel):
    WorkerExperience_id: int
    experience_id: int


class CreateWorkerExperienceID(CreateWorkerExperience):
    idWorkerExperience: int
