from sqlalchemy import create_engine
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

    with Session(autoflush=False, bind=ENGINE) as db:
        item = md.House(**params)

        db.add(item)
        db.commit()
        return item.id


def insert_in_HouseEquip(**params):
    md.Base.metadata.create_all(bind=ENGINE)

    with Session(autoflush=False, bind=ENGINE) as db:
        item = md.HouseEquip(**params)

        db.add(item)
        db.commit()
        return item.id


def read_from_Person(**params):

    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(md.Person).filter_by(**params).first()
        return item.id


def read_from_Organization(**params):

    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(md.Organization).filter_by(**params).first()
        return item.id


def read_from_House(**params):

    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(md.House).filter_by(**params).first()
        return item.id


def read_from_HouseEquip(**params):

    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(md.HouseEquip).filter_by(**params).first()
        return item.id


def update_in_Person(**params):

    with Session(autoflush=False, bind=ENGINE) as db:

        item = db.query(md.Person).filter(md.Person.id == params["id"]).first()

        if (item != None):
            print(item.id, item.family_name, item.name)

            for key, value in params.items():
                if key == "id":
                    continue
                if getattr(item, key) == value:
                    continue
                else:
                    setattr(item, key, value)

            db.commit()


def update_in_Organization(**params):
    with Session(autoflush=False, bind=ENGINE) as db:

        item = db.query(md.Organization).filter(
            md.Organization.id == params["id"]).first()

        if (item != None):
            for key, value in params.items():
                if key == "id":
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

                # Если первичный ключ, то пропускаем
                if key == "id" or key == "id_house":
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

                # if key == "client_id":
                #     house_owner = db.query(md.HouseOwner).filter(
                #         md.HouseOwner.id_house == params["id_house"]).first()

                #     if house_owner == None:
                #         return "ERROR"

                #     if house_owner.id_person == params["client_id"]:
                #         continue
                #     else:
                #         house_owner.id_person = params["client_id"]
                #         continue

                if key == "is_actual":
                    house_owner = db.query(md.HouseOwner).filter(
                        md.HouseOwner.id_house == params["id_house"]).first()

                    if house_owner == None:
                        return "ERROR"

                    if house_owner.is_actual == params["is_actual"]:
                        continue
                    else:
                        house_owner.is_actual = params["is_actual"]
                        continue

                if getattr(house, key) == value:
                    continue
                else:
                    setattr(house, key, value)

            db.commit()


def update_in_HouseEquip(**params):
    with Session(autoflush=False, bind=ENGINE) as db:

        item = db.query(md.HouseEquip).filter(
            md.HouseEquip.id == params["id"]).first()

        if (item != None):
            for key, value in params.items():
                if key == "id":
                    continue
                if getattr(item, key) == value:
                    continue
                else:
                    setattr(item, key, value)

            db.commit()


def delete_from_Person(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(md.Person).filter(
            md.Person.id == params["id"]).first()
        if item == None:
            return "ERROR"
        db.delete(item)
        db.commit()


def delete_from_Organization(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(md.Organization).filter(
            md.Organization.id == params["id"]).first()
        if item == None:
            return "ERROR"
        db.delete(item)
        db.commit()


def delete_from_House(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(md.House).filter(
            md.House.id == params["id"]).first()
        if item == None:
            return "ERROR"
        db.delete(item)
        db.commit()


def delete_from_HouseEquip(**params):
    with Session(autoflush=False, bind=ENGINE) as db:
        item = db.query(md.HouseEquip).filter(
            md.HouseEquip.id == params["id"]).first()
        if item == None:
            return "ERROR"
        db.delete(item)
        db.commit()
