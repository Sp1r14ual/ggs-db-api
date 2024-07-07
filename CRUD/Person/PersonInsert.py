from Models.BaseModel import Base as BaseMD
from Models.PersonModel import Person as PersonMD
from sqlalchemy.orm import Session
from CRUD.Engine import ENGINE


def insert_in_Person(**params):

    BaseMD.metadata.create_all(bind=ENGINE)

    with Session(autoflush=False, bind=ENGINE) as db:
        item = PersonMD(**params)

        db.add(item)
        db.commit()
        return item.id
