from models.person_model import Person as PersonMD
from sqlalchemy.orm import Session
from db.engine import ENGINE


def delete_from_Person(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(PersonMD).filter(
            PersonMD.id == params["id_client"]).first()
        if item == None:
            return "ERROR"
        db.delete(item)
        db.commit()
