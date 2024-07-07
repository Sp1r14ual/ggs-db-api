from Models.BaseModel import Base as BaseMD
from Models.HouseModel import House as HouseMD
from Models.HouseOwnerModel import HouseOwner as HouseOwnerMD
from Models.TownModel import Town as TownMD
from Models.DisctrictModel import District as DistrictMD
from Models.StreetModel import Street as StreetMD
from sqlalchemy.orm import Session
from CRUD.Engine import ENGINE


def insert_in_House(**params):

    BaseMD.metadata.create_all(bind=ENGINE)

    house_params = dict()
    house_owner_params = dict()

    with Session(autoflush=False, bind=ENGINE) as db:
        for key, value in params.items():
            if key == "adress":
                continue
            if key in ("id_client", "is_actual"):
                if key == "id_client":
                    house_owner_params["id_person"] = value
                else:
                    house_owner_params[key] = value
            else:
                # house_params[key] = value
                if key == "town":
                    town = db.query(TownMD).filter(
                        TownMD.name == params["town"]).first()

                    if town == None:
                        return "ERROR"

                    house_params["id_town"] = town.id

                if key == "district":
                    district = db.query(DistrictMD).filter(
                        DistrictMD.name == params["district"]).first()

                    if district == None:
                        return "ERROR"

                    house_params["id_district"] = district.id

                if key == "street":
                    street = db.query(StreetMD).filter(
                        StreetMD.name == params["street"]).first()

                    if street == None:
                        return "ERROR"

                    house_params["id_street"] = street.id

        house = HouseMD(**house_params)
        db.add(house)
        db.commit()

        print("HOUSE_ID:", house.id)
        house_owner_params["id_house"] = house.id
        house_owner = HouseOwnerMD(**house_owner_params)
        db.add(house_owner)
        db.commit()

        return house.id
