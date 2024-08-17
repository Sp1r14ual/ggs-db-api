from models.house_equip_model import HouseEquip as HouseEquipMD
from sqlalchemy.orm import Session
from sqlalchemy import and_
from db.engine import ENGINE


def delete_from_HouseEquip(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(HouseEquipMD).filter(and_(
            HouseEquipMD.id == params["id_house_equip"], HouseEquipMD.id_house == params["id_house"])).first()

        if item == None:
            return "Error: House Equip does not exist"

        db.delete(item)
        db.commit()
