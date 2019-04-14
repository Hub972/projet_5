# usr/bin/python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, INTEGER, VARCHAR, BIGINT, SMALLINT
from sqlalchemy.ext.declarative import declarative_base


sql = create_engine('mysql+mysqldb://root:""@localhost/project5') # set the data base to use
Base = declarative_base() # for create the db.
con = sql.connect() # for connect to db.
trans = con.begin() # for transaction with the db.


class Products(Base):
    """Create model for table"""
    __tablename__ = 'products'
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(250))
    generic_name = Column(VARCHAR(250))
    bar_code = Column(BIGINT)
    cat = Column(VARCHAR(10))
    alter_code = Column(BIGINT)
    is_subtitute = Column(SMALLINT)


def load_tables():
    """create table about the model"""
    Base.metadata.create_all(sql)


