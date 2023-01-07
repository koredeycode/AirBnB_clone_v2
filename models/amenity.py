#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models


class Amenity(BaseModel, Base):
    '''amenity class'''
    __tablename__ = 'amenities'
    if models.storage_type == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
