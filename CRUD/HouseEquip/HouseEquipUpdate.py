from Models.HouseEquipModel import HouseEquip as HouseEquipMD
from sqlalchemy.orm import Session
from CRUD.Engine import ENGINE


def update_in_HouseEquip(**params):
    with Session(autoflush=False, bind=ENGINE) as db:

        item = db.query(HouseEquipMD).filter(
            HouseEquipMD.id == params["id_house_equip"]).first()

        if (item != None):
            for key, value in params.items():
                if key == "id_house_equip":
                    continue
                if key == "house_id":
                    item.id_house = value
                    continue
                if getattr(item, key) == value:
                    continue
                else:
                    setattr(item, key, value)

            db.commit()

        else:
            return "ERROR"
