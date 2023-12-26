from fastapi import FastAPI
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


@app.post("/user/", response_model=CreateUserID)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    new_user = Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/worker/", response_model=CreateWorkerID)
def create_worker(worker: CreateWorker, db: Session = Depends(get_db)):
    new_worker = Workers(**worker.dict())
    db.add(new_worker)
    db.commit()
    db.refresh(new_worker)
    return new_worker