from models.house_equip_model import HouseEquip as HouseEquipMD
from sqlalchemy.orm import Session
from db.engine import ENGINE


def delete_from_HouseEquip(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(HouseEquipMD).filter(
            HouseEquipMD.id == params["id_house_equip"]).first()
        if item == None:
            return "ERROR"
        db.delete(item)
        db.commit()
