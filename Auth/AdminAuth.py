from Models.AdminModel import Admin as AdminMD
from sqlalchemy.orm import Session
from CRUD.Engine import ENGINE


def authenticate(username: str) -> bool:
    with Session(autoflush=False, bind=ENGINE) as db:

        admin = db.query(AdminMD).filter(AdminMD.login == username).first()

        return True if admin else False
