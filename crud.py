from sqlalchemy import create_engine, and_
from sqlalchemy.orm import Session
import models as md

ENGINE = create_engine(
    'mssql+pyodbc://DESKTOP-4KRGT6O\\SQLEXPRESS/ggs_stud?driver=SQL+Server+Native+Client+11.0', echo=True)


def insert_in_Person(**params):

    md.Base.metadata.create_all(bind=ENGINE)

    with Session(autoflush=False, bind=ENGINE) as db:
        item = md.Person(**params)

        db.add(item)
        db.commit()
        return item.id


def insert_in_Organization(**params):

    md.Base.metadata.create_all(bind=ENGINE)

    with Session(autoflush=False, bind=ENGINE) as db:
        item = md.Organization(**params)

        db.add(item)
        db.commit()
        return item.id


def insert_in_House(**params):

    md.Base.metadata.create_all(bind=ENGINE)

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
                    town = db.query(md.Town).filter(
                        md.Town.name == params["town"]).first()

                    if town == None:
                        return "ERROR"

                    house_params["id_town"] = town.id

                if key == "district":
                    district = db.query(md.District).filter(
                        md.District.name == params["district"]).first()

                    if district == None:
                        return "ERROR"

                    house_params["id_district"] = district.id

                if key == "street":
                    street = db.query(md.Street).filter(
                        md.Street.name == params["street"]).first()

                    if street == None:
                        return "ERROR"

                    house_params["id_street"] = street.id

        house = md.House(**house_params)
        db.add(house)
        db.commit()

        print("HOUSE_ID:", house.id)
        house_owner_params["id_house"] = house.id
        house_owner = md.HouseOwner(**house_owner_params)
        db.add(house_owner)
        db.commit()

        return house.id


def insert_in_HouseEquip(**params):
    md.Base.metadata.create_all(bind=ENGINE)

    with Session(autoflush=False, bind=ENGINE) as db:
        item = md.HouseEquip(**params)

        db.add(item)
        db.commit()
        return item.id


def update_in_Person(**params):

    with Session(autoflush=False, bind=ENGINE) as db:

        item = db.query(md.Person).filter(
            md.Person.id == params["client_id"]).first()

        if (item != None):
            for key, value in params.items():
                if key == "client_id":
                    continue
                if getattr(item, key) == value:
                    continue
                else:
                    setattr(item, key, value)

            db.commit()


def update_in_Organization(**params):
    with Session(autoflush=False, bind=ENGINE) as db:

        item = db.query(md.Organization).filter(
            md.Organization.id == params["organization_id"]).first()

        if (item != None):
            for key, value in params.items():
                if key == "organization_id":
                    continue
                if getattr(item, key) == value:
                    continue
                else:
                    setattr(item, key, value)

            db.commit()


def update_in_House(**params):
    with Session(autoflush=False, bind=ENGINE) as db:

        house = db.query(md.House).filter(
            md.House.id == params["id_house"]).first()

        house_owner = None

        if (house != None):
            for key, value in params.items():
                if key == "id" or key == "id_house" or key == "id_client":
                    continue

                if key == "adress":
                    continue

                if key == "town":
                    town = db.query(md.Town).filter(
                        md.Town.name == params["town"]).first()

                    if town == None:
                        return "ERROR"

                    if house.id_town == town.id:
                        continue
                    else:
                        house.id_town = town.id
                        continue

                if key == "district":
                    district = db.query(md.District).filter(
                        md.District.name == params["district"]).first()

                    if district == None:
                        return "ERROR"

                    if house.id_district == district.id:
                        continue
                    else:
                        house.id_district = district.id
                        continue

                if key == "street":
                    street = db.query(md.Street).filter(
                        md.Street.name == params["street"]).first()

                    if street == None:
                        return "ERROR"

                    if house.id_street == street.id:
                        continue
                    else:
                        house.id_street = street.id
                        continue

                if key == "is_actual":
                    house_owner = db.query(md.HouseOwner).filter(and_(
                        md.HouseOwner.id_house == params["id_house"], md.HouseOwner.id_person == params["id_client"])).first()

                    if house_owner == None:
                        return "ERROR"

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


def update_in_HouseEquip(**params):
    with Session(autoflush=False, bind=ENGINE) as db:

        item = db.query(md.HouseEquip).filter(
            md.HouseEquip.id == params["id_house_equip"]).first()

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


def delete_from_Person(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(md.Person).filter(
            md.Person.id == params["id_client"]).first()
        if item == None:
            return "ERROR"
        db.delete(item)
        db.commit()


def delete_from_Organization(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(md.Organization).filter(
            md.Organization.id == params["id_organization"]).first()
        if item == None:
            return "ERROR"
        db.delete(item)
        db.commit()


def delete_from_House(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(md.House).filter(
            md.House.id == params["id_house"]).first()
        if item == None:
            return "ERROR"
        db.delete(item)
        db.commit()


def delete_from_HouseEquip(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(md.HouseEquip).filter(
            md.HouseEquip.id == params["id_house_equip"]).first()
        if item == None:
            return "ERROR"
        db.delete(item)
        db.commit()
