from models.base_model import Base as BaseMD
from models.house_equip_model import HouseEquip as HouseEquipMD
from models.abonent_model import Abonent as AbonentMD
from sqlalchemy.orm import Session
from db.engine import ENGINE


def insert_in_HouseEquip(**params):
    BaseMD.metadata.create_all(bind=ENGINE)

    abonent_params = dict()
    house_equip_params = dict()

    with Session(autoflush=False, bind=ENGINE) as db:

        for key, value in params.items():
            if key == "id_client":
                abonent_params["id_person"] = value
                abonent_params["id_type_abonent"] = 1
                abonent_params["id_house"] = params["id_house"]
            elif key == "id_organization":
                abonent_params["id_organization"] = value
                abonent_params["id_type_abonent"] = 2
                abonent_params["id_house"] = params["id_house"]
            else:
                house_equip_params[key] = value

        abonent = AbonentMD(**abonent_params)
        db.add(abonent)
        db.commit()

        house_equip_params["id_abonent"] = abonent.id
        house_equip = HouseEquipMD(**house_equip_params)

        db.add(house_equip)
        db.commit()
        return house_equip.id
