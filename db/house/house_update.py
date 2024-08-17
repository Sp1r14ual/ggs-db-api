from sqlalchemy import and_
from models.organization_model import Organization as OrganizationMD
from models.house_model import House as HouseMD
from models.house_owner_model import HouseOwner as HouseOwnerMD
from models.town_model import Town as TownMD
from models.disctrict_model import District as DistrictMD
from models.street_model import Street as StreetMD
from sqlalchemy.orm import Session
from db.engine import ENGINE


def update_in_House(**params):
    with Session(autoflush=False, bind=ENGINE) as db:

        house = db.query(HouseMD).filter(
            HouseMD.id == params["id_house"]).first()

        house_owner = None

        if (house != None):
            for key, value in params.items():
                if key == "id" or key == "id_house" or key == "id_client":
                    continue

                if key == "adress":
                    continue

                if key == "town":
                    town = db.query(TownMD).filter(
                        TownMD.name == params["town"]).first()

                    if town == None:
                        return "Error: Town does not exist"

                    if house.id_town == town.id:
                        continue
                    else:
                        house.id_town = town.id
                        continue

                if key == "district":
                    district = db.query(DistrictMD).filter(
                        DistrictMD.name == params["district"]).first()

                    if district == None:
                        return "Error: District does not exist"

                    if house.id_district == district.id:
                        continue
                    else:
                        house.id_district = district.id
                        continue

                if key == "street":
                    street = db.query(StreetMD).filter(
                        StreetMD.name == params["street"]).first()

                    if street == None:
                        return "Error: Street does not exist"

                    if house.id_street == street.id:
                        continue
                    else:
                        house.id_street = street.id
                        continue

                if key == "id_organization":
                    organization = db.query(OrganizationMD).filter(
                        OrganizationMD.id == params["id_organization"]).first()

                    if organization == None:
                        return "Error: Organization does not exist"

                if key == "is_actual":

                    try:
                        params["id_client"]
                    except KeyError:
                        continue

                    house_owner = db.query(HouseOwnerMD).filter(and_(
                        HouseOwnerMD.id_house == params["id_house"], HouseOwnerMD.id_person == params["id_client"])).first()

                    if house_owner == None:
                        return "Error: House Owner does not exist"

                    if getattr(house_owner, key) == value:
                        continue
                    else:
                        setattr(house_owner, key, value)
                        continue

                if getattr(house, key) == value:
                    continue
                else:
                    setattr(house, key, value)

            db.commit()

        else:
            return "Error: House does not exist"
