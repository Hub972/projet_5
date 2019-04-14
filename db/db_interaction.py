# usr/bin/python3
# -*- coding: utf-8 -*-


import sqlalchemy
from sqlalchemy.orm import sessionmaker

from .db_engine import sql, Products, con, trans

Session = sessionmaker(bind=sql)


class Interaction:
    def __init__(self):
        self.session = Session()
        self.con = con
        self.trans = trans

    def changeProduct(self, name, pid):
        """This method use the sql syntax for update the table"""
        product = self.session.query(Products).filter(Products.id == pid)
        for pr in product:
            old_code = str(pr.bar_code) # search the bar code of product to substitute.
        for pr in product:
            sub = pr.is_subtitute # search the 'is_substitute' value.
        for pr in product:
            new_code = str(pr.alter_code) # search the new bar code product.
        stid = str(pid)
        if sub == 0:
            """If sub=0, execute the update and is_substitute=1 else is_substitute=0."""
            self.con.execute(
                f"UPDATE products SET name = '{name}', bar_code =" + str(new_code) + ",\
                 alter_code=" + str(old_code) + ",\
                 is_subtitute = 1 WHERE id =" + stid)
        else:
            self.con.execute(
                f"UPDATE products SET name = '{name}', bar_code =" + str(new_code) + ",\
                 alter_code=" + str(old_code) + ",\
                 is_subtitute = 0 WHERE id =" + stid)
        try:
            self.trans.commit()
        except sqlalchemy.exc.InvalidRequestError:
            self.trans.rollback()
            self.trans = trans # reinitialize the transaction

    def addListProducts(self):
        """List of products to load in the database"""
        listProducts = [("Confiture abricot", "Confiture abricot", 3324498000746, 2, 3760121210661, 0), \
                        ("Confiture pomme au calvados", "Confiture pomme au calvados", 3324498002542, 2, 3396745001110 \
                             , 0), \
                        ("Yaourt Brassé", "Yaourt brassé nature", 26065250, 2, 3222474051228, 0), \
                        ("Tomates Farcies et Riz Long Blanc", "Tomates Farcies et Riz Long Blanc", 3258561470641, 1, \
                         3248830690214, 0), \
                        ("Crème fraîche légère épaisse", "Crème fraîche légère épaisse", 3700311861334, 1, \
                         3382322220005, 0), \
                        ("Pavé de Saumon ASC", "Pavé de Saumon ", 40884004, 1, 3270160741939, 0), \
                        ("Rillettes de Poulet Rôti en Cocotte", "Rillettes de Poulet Rôti", 3560070507832, 1, \
                         3250391554508, 0), \
                        ("Cidre Brut", "Cidre Brut", 3186630000973, 3, 20466268, 0), \
                        ("Nectar Multifruits", "Jus Multifruit", 3270190128410, 3, 3254691586054, 0), \
                        ("Nuggets de Poulet", "Préparation à base de viande de poulet et de dinde traitée en salaison \
                        reconstituée (60%)", 3222472621218, 1, 3422210446190, 0)]
        for a, b, c, d, e, f in listProducts:
            name = Products(name="{}".format(a), generic_name="{}".format(b), bar_code=c, cat=d, alter_code=e, \
                            is_subtitute=f)
            self.session.add(name)
            self.session.commit()
            print("Produits ajouté")

    def displayTable(self, table, inner, subt):
        """Display a list of product about a specific filter """
        if subt == 0:
            """About the category"""
            dsply = self.session.query(table) \
                .filter(table.cat == inner)
        else:
            """About the substituted products"""
            dsply = self.session.query(table) \
                .filter(table.is_subtitute == 1)
        l_id = []
        for pr in dsply:
            l_id.append(pr.id)
            print("##########################################")
            print(f"{pr.id}, {pr.name}, {pr.bar_code}")
            print("##########################################")
        if subt != 0:
            input("Taper 'Entrée' pour sortir:")
        else:
            choice = input("Tapez 00 pou revenir aux catégories ou Entrée pour continuer:")
            if choice == "00":
                qut1 = "q" # Value for back in  the previous.
                return qut1
        self.session = Session() # reinitialize the session.
        return l_id # Return a list of id products.


