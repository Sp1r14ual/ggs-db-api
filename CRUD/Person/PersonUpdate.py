from Models.PersonModel import Person as PersonMD
from sqlalchemy.orm import Session
from CRUD.Engine import ENGINE


def update_in_Person(**params):

    with Session(autoflush=False, bind=ENGINE) as db:

        item = db.query(PersonMD).filter(
            PersonMD.id == params["client_id"]).first()

        if (item != None):
            for key, value in params.items():
                if key == "client_id":
                    continue
                if getattr(item, key) == value:
                    continue
                else:
                    setattr(item, key, value)

            db.commit()

        else:
            return "ERROR"
