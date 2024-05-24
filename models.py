from sqlalchemy import Column, Integer, CHAR, DateTime, VARCHAR, NVARCHAR
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = 'person'
    __table_args__ = {'implicit_returning': False}

    id = Column(Integer, primary_key=True, nullable=False)
    family_name = Column(VARCHAR(1024), nullable=False, default="Doe")
    birthdate = Column(DateTime, nullable=True)
    phone_number = Column(VARCHAR(16), nullable=True)
    name = Column(VARCHAR(1024), nullable=False, default="John")
    patronimic_name = Column(VARCHAR(1024), nullable=True)
    pasport_serial = Column(VARCHAR(6), nullable=True)
    pasport_number = Column(VARCHAR(12), nullable=True)
    pasport_date = Column(DateTime, nullable=True)
    pasport_place = Column(VARCHAR(512), nullable=True)
    remark = Column(VARCHAR(512), nullable=True)
    dep_code = Column(VARCHAR(6), nullable=True)
    reg_adress = Column(VARCHAR(1024), nullable=True)
    reg_region = Column(VARCHAR(200), nullable=True)
    reg_raion = Column(VARCHAR(200), nullable=True)
    reg_city = Column(VARCHAR(200), nullable=True)
    reg_street = Column(VARCHAR(200), nullable=True)
    reg_house = Column(VARCHAR(200), nullable=True)
    reg_flat = Column(VARCHAR(20), nullable=True)
    postal_index = Column(VARCHAR(6), nullable=True)
    inn = Column(VARCHAR(16), nullable=True)
    ogrn = Column(VARCHAR(32), nullable=True)
    snils = Column(VARCHAR(32), nullable=True)
    email = Column(VARCHAR(32), nullable=True)


class Organization(Base):
    __tablename__ = 'organization'
    __table_args__ = {'implicit_returning': False}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(VARCHAR(1024), nullable=False, default="DEFAULT_COMPANY")
    adress_jur = Column(VARCHAR(1024), nullable=True)
    zip_code_jur = Column(VARCHAR(6), nullable=True)
    adress_fact = Column(VARCHAR(1024), nullable=True)
    zip_code_fact = Column(VARCHAR(6), nullable=True)
    is_coop = Column(Integer, nullable=False, default=0)
    is_pir = Column(Integer, nullable=False, default=0)
    is_smr_gvd_gnd = Column(Integer, nullable=False, default=0)
    is_smr_vdgo = Column(Integer, nullable=False, default=0)
    is_to_gvd_gnd = Column(Integer, nullable=False, default=0)
    remark = Column(VARCHAR(1024), nullable=True)
    inn = Column(CHAR(12), nullable=True)
    kpp = Column(CHAR(9), nullable=True)
    bik = Column(CHAR(9), nullable=True)
    korr_acc = Column(CHAR(20), nullable=True)
    calc_acc = Column(CHAR(20), nullable=True)
    bank = Column(VARCHAR(128), nullable=True)
    is_gro = Column(Integer, nullable=True)
    ogrn = Column(VARCHAR(32), nullable=True)
    from_1c = Column(Integer, nullable=False, default=0)
    to_rg = Column(Integer, nullable=False, default=0)
    to_ggs = Column(Integer, nullable=False, default=0)
    to_gss = Column(Integer, nullable=False, default=0)
    to_ggsi = Column(Integer, nullable=False, default=0)
    to_ggss = Column(Integer, nullable=False, default=0)
    to_rgs = Column(Integer, nullable=False, default=0)


class House(Base):
    __tablename__ = 'house'
    __table_args__ = {'implicit_returning': False}

    id = Column(Integer, primary_key=True, nullable=False)
    cadastr_number = Column(VARCHAR(32), nullable=True)
    # Что делать с остальными полями?


class HouseEquip(Base):
    __tablename__ = 'house_equip'
    __table_args__ = {'implicit_returning': False}

    id = Column(Integer, primary_key=True, nullable=False)

    # в мануале id_client, а в БД id_abonent?
    id_abonent = Column(Integer, nullable=True)
    id_house = Column(Integer, nullable=True)
    id_type_house_equip = Column(Integer, nullable=True)
    year_produce = Column(Integer, nullable=True)
    remark = Column(VARCHAR(128), nullable=True)

    # в БД нет поля id_house_equip
    # id_house_equip - это просто первичный ключ id из таблицы?
