from models.base_model import Base as BaseMD
from models.organization_model import Organization as OrganizationMD
from models.house_model import House as HouseMD
from models.house_owner_model import HouseOwner as HouseOwnerMD
from models.town_model import Town as TownMD
from models.disctrict_model import District as DistrictMD
from models.street_model import Street as StreetMD
from sqlalchemy.orm import Session
from db.engine import ENGINE


def insert_in_House(**params):

    BaseMD.metadata.create_all(bind=ENGINE)

    house_params = dict()
    house_owner_params = dict()

    with Session(autoflush=False, bind=ENGINE) as db:
        for key, value in params.items():
            if key == "adress":
                continue
            elif key in ("id_client", "id_organization"):
                if key == "id_client":
                    house_owner_params["id_person"] = value
                    house_owner_params["is_actual"] = value
                else:
                    organization = db.query(OrganizationMD).filter(
                        OrganizationMD.id == params["id_organization"]).first()

                    if organization == None:
                        return "Error: Organization does not exist"

                    house_params["id_organization"] = organization.id

            else:
                # house_params[key] = value
                if key == "town":
                    town = db.query(TownMD).filter(
                        TownMD.name == params["town"]).first()

                    if town == None:
                        return "Error: Town does not exist"

                    house_params["id_town"] = town.id

                if key == "district":
                    district = db.query(DistrictMD).filter(
                        DistrictMD.name == params["district"]).first()

                    if district == None:
                        return "Error: District does not exist"

                    house_params["id_district"] = district.id

                if key == "street":
                    street = db.query(StreetMD).filter(
                        StreetMD.name == params["street"]).first()

                    if street == None:
                        return "Error: Street does not exist"

                    house_params["id_street"] = street.id

        house = HouseMD(**house_params)
        db.add(house)
        db.commit()

        try:
            params["id_client"]
        except KeyError:
            return house.id

        # print("HOUSE_ID:", house.id)
        house_owner_params["id_house"] = house.id
        house_owner = HouseOwnerMD(**house_owner_params)
        db.add(house_owner)
        db.commit()

        return house.id
