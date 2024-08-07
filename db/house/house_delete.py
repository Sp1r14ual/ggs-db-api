from models.house_model import House as HouseMD
from sqlalchemy.orm import Session
from db.engine import ENGINE


def delete_from_House(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(HouseMD).filter(
            HouseMD.id == params["id_house"]).first()
        if item == None:
            return "ERROR"
        db.delete(item)
        db.commit()
