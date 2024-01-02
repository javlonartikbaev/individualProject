from typing import List

from fastapi import FastAPI, HTTPException, status
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI, Depends, HTTPException
from database.database import *
from models.models import *


DATABASE_URL = "mysql+pymysql://root:qwerty123@localhost:3306/DatabaseHH"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


# ----------------------------------------- Create user -----------------------------------------
@app.post("/user/", response_model=CreateUserID)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    new_user = Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# ----------------------------------- Create Worker -----------------------------------------------------
@app.post("/worker/", response_model=CreateWorkerID)
def create_worker(worker: CreateWorker, db: Session = Depends(get_db)):
    new_worker = Workers(**worker.dict())
    db.add(new_worker)
    db.commit()
    db.refresh(new_worker)
    return new_worker


# ----------------------------------- Список всех работников --------------------------


@app.get("/workers/", response_model=List[CreateWorker])
def get_workers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    workers = db.query(Workers).offset(skip).limit(limit).all()
    return workers


# ------------------------------------ Удаление работника  ------------------------------------------
@app.delete("/workers/{id}", response_model=CreateWorker)
def delete_worker(worker_id: int, db: Session = Depends(get_db)):
    worker = db.query(Workers).filter(Workers.idWorkers == worker_id).first()
    if not worker:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(worker)
    db.commit()
    return worker


# ----------------------------------- Create Citizenship -----------------------------------------------------
@app.post("/citizenship/", response_model=CreateCitizenshipID)
def create_citizenship(citizenship: CreateCitizenship, db: Session = Depends(get_db)):
    citizenship = Citizenship(**citizenship.dict())
    db.add(citizenship)
    db.commit()
    db.refresh(citizenship)
    return citizenship


# ----------------------------------- Create Skills -----------------------------------------------------
@app.post("/skills/", response_model=CreateSkillID)
def create_skill(skill: CreateSkill, db: Session = Depends(get_db)):
    new_skill = Skill(**skill.dict())
    db.add(new_skill)
    db.commit()
    db.refresh(new_skill)
    return new_skill


# create Worker and Skill reletionship
@app.post("/skills{id}/", response_model=Worker_has_skill)
def create_skill_and_worker(
    workerSkill: Worker_has_skill, db: Session = Depends(get_db)
):
    workerWithskill = WorkerAndSkill(**workerSkill.dict())
    db.add(workerWithskill)
    db.commit()
    db.refresh(workerWithskill)
    return workerWithskill


# --------------------------------------------------------------------------------------------------------


# ------------------------------ Create Profession -------------------------------------------------------
@app.post("/profession/", response_model=CreateProfessionID)
def create_profession(profession: CreateProfession, db: Session = Depends(get_db)):
    new_profession = ProfessionOrm(**profession.dict())
    db.add(new_profession)
    db.commit()
    db.refresh(new_profession)
    return new_profession


@app.post("/profession{id}/", response_model=ProfessionCategoriesID)
def create_profession_categories(
    profession_categories: ProfessionCategories, db: Session = Depends(get_db)
):
    new_profession_categories = ProfessionCategoriesORM(**profession_categories.dict())
    db.add(new_profession_categories)
    db.commit()
    db.refresh(new_profession_categories)
    return new_profession_categories


@app.post("/categories/", response_model=CreateCategoriesID)
def categories(new_categories: CreateCategories, db: Session = Depends(get_db)):
    new_categories = CategorisOrm(**new_categories.dict())
    db.add(new_categories)
    db.commit()
    db.refresh(new_categories)
    return new_categories


# ---------------------------------------------------------------------------------------------------
# ----------------------------- University and Education --------------------------------------------


@app.post("/university/", response_model=CreateUniversityID)
def university(new_university: CreateUniversity, db: Session = Depends(get_db)):
    new_university = UniversityORM(**new_university.dict())
    db.add(new_university)
    db.commit()
    db.refresh(new_university)
    return new_university


@app.post("/education/", response_model=CreateEducationID)
def education(new_education: CreateEducation, db: Session = Depends(get_db)):
    new_education = EducationORM(**new_education.dict())
    db.add(new_education)
    db.commit()
    db.refresh(new_education)
    return new_education


@app.post("/univerEducation{id}/", response_model=CreateUniversityEducationID)
def univerEducation(
    univerEducation: CreateUniversityEducation, db: Session = Depends(get_db)
):
    univerEducation = UniversityEducationORM(**univerEducation.dict())
    db.add(univerEducation)
    db.commit()
    db.refresh(univerEducation)
    return univerEducation


@app.post("/workerEducation/", response_model=CreateWorkerUniversityEducationID)
def workerEducation(
    workerEducation: CreateWorkerUniversityEducation, db: Session = Depends(get_db)
):
    workerEducation = WorkerUniversityEducationORM(**workerEducation.dict())
    db.add(workerEducation)
    db.commit()
    db.refresh(workerEducation)
    return workerEducation


@app.post("/experience/", response_model=CreateExperienceID)
def experience(experience: CreateExperience, db: Session = Depends(get_db)):
    new_experience = ExperienceORM(**experience.dict())
    db.add(new_experience)
    db.commit()
    db.refresh(new_experience)
    return new_experience


@app.post("/workerExperience/", response_model=CreateWorkerExperienceID)
def workerExperience(
    workerExperience: CreateWorkerExperience, db: Session = Depends(get_db)
):
    new_workerExperience = WorkerExperienceORM(**workerExperience.dict())
    db.add(new_workerExperience)
    db.commit()
    db.refresh(new_workerExperience)
    return new_workerExperience
