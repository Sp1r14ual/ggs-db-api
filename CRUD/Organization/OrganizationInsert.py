from Models.BaseModel import Base as BaseMD
from Models.OrganizationModel import Organization as OrganizationMD
from sqlalchemy.orm import Session
from CRUD.Engine import ENGINE


def insert_in_Organization(**params):

    BaseMD.metadata.create_all(bind=ENGINE)

    with Session(autoflush=False, bind=ENGINE) as db:
        item = OrganizationMD(**params)

        db.add(item)
        db.commit()
        return item.id
