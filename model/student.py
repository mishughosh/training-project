from db import base
from sqlalchemy import Column, Integer, String

class Students(base):
    __tablename__ ="Std_Table"

    id = Column(Integer, primary_key= True, index= True)
    name = Column(String(100))
    age = Column(Integer)
    email =Column(String(100))
    roll = Column(Integer, unique= True)
    session = Column(String(20))
    