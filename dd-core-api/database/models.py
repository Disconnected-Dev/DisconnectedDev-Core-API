#!/usr/bin/env python3

from sqlalchemy import Boolean, column, ForeignKey, Integer, String
from database import Base


class Blog(Base):
    __tablename__ = 'blog'

    bID = Column(Integer, primary_key=True, index=True)
    bTitle = Column(String, index=True)
    bText = Column(String, index=True)
    bCount = Column(Integer, index=True)
    bDT = column(String, index=True)


class users(Base):
    __tablename__ = 'users'

    uID = Column(Integer, primary_key=True, index=True)
    uName = Column(String, index=True)
    uFurname = Column(String, index=True)
    uForename = Column(String, index=true)
    uRegDate = Column(String, index=True)
