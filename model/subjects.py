from db import base
from sqlalchemy import Column, String, Integer

class Subjects(base):
    __tablename__ = "Sub_Table"

    id = Column(Integer, primary_key= True)
    student_roll = Column(Integer, unique= True)
    english_score = Column(Integer)
    math_score = Column(Integer)
    history_score = Column(Integer)
