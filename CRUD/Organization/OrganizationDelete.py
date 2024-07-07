from Models.OrganizationModel import Organization as OrganizationMD
from sqlalchemy.orm import Session
from CRUD.Engine import ENGINE


def delete_from_Organization(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(OrganizationMD).filter(
            OrganizationMD.id == params["id_organization"]).first()
        if item == None:
            return "ERROR"
        db.delete(item)
        db.commit()
