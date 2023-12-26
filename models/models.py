

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
    phoneNumber: str
    user_idUser: int


class CreateWorkerID(CreateWorker):
    idWorkers: int

# ---------------------------------------------------------------------------------------------