from models.house_model import House as HouseMD
from models.house_owner_model import HouseOwner as HouseOwnerMD
from sqlalchemy.orm import Session
from db.engine import ENGINE


def delete_from_House(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        house = db.query(HouseMD).filter(
            HouseMD.id == params["id_house"]).first()

        if house == None:
            return "Error: House does not exist"

        house_owner = db.query(HouseOwnerMD).filter(
            HouseOwnerMD.id_house == params["id_house"]).first()

        if house_owner != None:
            db.delete(house_owner)

        db.delete(house)
        db.commit()
