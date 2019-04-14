# usr/bin/python3
# -*- coding: utf-8 -*-


from db_interaction import Interaction
from db_engine import load_tables


def main():
    """Use for add products, don't forget set the engine db"""
    load_db = Interaction()
    load_db.addListProducts()


def createTable():
    """Load the table"""
    load_tables()


if __name__ == '__main__':
    createTable()
    main()
