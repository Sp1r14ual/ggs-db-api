from Models.BaseModel import Base as BaseMD
from Models.HouseEquipModel import HouseEquip as HouseEquipMD
from sqlalchemy.orm import Session
from CRUD.Engine import ENGINE


def insert_in_HouseEquip(**params):
    BaseMD.metadata.create_all(bind=ENGINE)

    with Session(autoflush=False, bind=ENGINE) as db:
        item = HouseEquipMD(**params)

        db.add(item)
        db.commit()
        return item.id
