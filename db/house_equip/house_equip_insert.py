from models.base_model import Base as BaseMD
from models.house_equip_model import HouseEquip as HouseEquipMD
from sqlalchemy.orm import Session
from db.engine import ENGINE


def insert_in_HouseEquip(**params):
    BaseMD.metadata.create_all(bind=ENGINE)

    with Session(autoflush=False, bind=ENGINE) as db:
        item = HouseEquipMD(**params)

        db.add(item)
        db.commit()
        return item.id
