from sqlalchemy import Column, NVARCHAR, DateTime, Integer
from Models.BaseModel import Base


class Admin(Base):
    __tablename__ = 'admin_logins'
    __table_args__ = {'implicit_returning': False}

    # column_not_exist_in_db = Column(Integer, primary_key=True)

    login = Column(NVARCHAR(64), primary_key=True, nullable=False)
    added = Column(DateTime, nullable=False)
