from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


class Item2(Base):
    __tablename__ = "items2"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)



class Item3(Base):
    __tablename__ = "items3"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)



class Item4(Base):
    __tablename__ = "items4"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)