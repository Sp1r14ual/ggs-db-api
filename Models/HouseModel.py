from sqlalchemy import Column, Integer, VARCHAR
from Models.BaseModel import Base


class House(Base):
    __tablename__ = 'house'
    __table_args__ = {'implicit_returning': False}

    id = Column(Integer, primary_key=True, nullable=False)

    # В БД nullable, а в мануале обязательный, как быть? Нужен default_value?
    # + сопоставить вторичный ключ с другой таблицей
    id_town = Column(Integer, nullable=True)

    # NULL/Не NULL + вторичный ключ
    id_district = Column(Integer, nullable=True)

    id_street = Column(Integer, nullable=True)  # NULL/Не NULL + вторичный ключ
    house_number = Column(VARCHAR(32), nullable=True)  # NULL/Не NULL
    corpus_number = Column(VARCHAR(32), nullable=True)  # NULL/Не NULL

    flat_number = Column(VARCHAR(12), nullable=True)
    cadastr_number = Column(VARCHAR(32), nullable=True)
    # Что делать с остальными полями?
