from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError
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

        item = db.query(md.House).filter(
            md.House.id == params["id"]).first()

        if (item != None):
            for key, value in params.items():
                if key == "id":
                    continue
                if getattr(item, key) == value:
                    continue
                else:
                    setattr(item, key, value)

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
