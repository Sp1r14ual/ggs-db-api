from models.organization_model import Organization as OrganizationMD
from sqlalchemy.orm import Session
from db.engine import ENGINE


def delete_from_Organization(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(OrganizationMD).filter(
            OrganizationMD.id == params["id_organization"]).first()

        if item == None:
            return "Error: Organization does not exist"

        db.delete(item)
        db.commit()
