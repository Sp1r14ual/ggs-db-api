from models.base_model import Base as BaseMD
from models.organization_model import Organization as OrganizationMD
from sqlalchemy.orm import Session
from db.engine import ENGINE


def insert_in_Organization(**params):

    BaseMD.metadata.create_all(bind=ENGINE)

    with Session(autoflush=False, bind=ENGINE) as db:
        item = OrganizationMD(**params)

        db.add(item)
        db.commit()
        return item.id
