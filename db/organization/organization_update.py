from models.organization_model import Organization as OrganizationMD
from sqlalchemy.orm import Session
from db.engine import ENGINE


def update_in_Organization(**params):
    with Session(autoflush=False, bind=ENGINE) as db:

        item = db.query(OrganizationMD).filter(
            OrganizationMD.id == params["organization_id"]).first()

        if (item != None):
            for key, value in params.items():
                if key == "organization_id":
                    continue
                if getattr(item, key) == value:
                    continue
                else:
                    setattr(item, key, value)

            db.commit()

        else:
            return "Error: Organization does not exist"
