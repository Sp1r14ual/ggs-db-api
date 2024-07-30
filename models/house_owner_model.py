from sqlalchemy import Column, Integer
from models.base_model import Base


class HouseOwner(Base):
    __tablename__ = 'house_owner'
    __table_args__ = {'implicit_returning': False, 'extend_existing': True}

    id = Column(Integer, primary_key=True, nullable=False)
    id_person = Column(Integer, nullable=False)  # default_value какое сделать?
    id_house = Column(Integer, nullable=False)  # Тоже самое
    # В БД Null, в мануале не нулл
    is_actual = Column(Integer, nullable=True)
