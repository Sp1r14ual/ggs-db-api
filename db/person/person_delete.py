from models.person_model import Person as PersonMD
from sqlalchemy.orm import Session
from db.engine import ENGINE


def delete_from_Person(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        person = db.query(PersonMD).filter(
            PersonMD.id == params["id_client"]).first()

        if not person:
            return "Error: Person does not exist"

        db.delete(person)
        db.commit()
