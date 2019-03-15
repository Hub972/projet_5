# usr/bin/python3
# -*- coding: utf-8 -*-


import requests

from db.db_interaction import Interaction


class Request(Interaction):
    def __init__(self):
        Interaction.__init__(self)

    def searchProductCode(self, code, id):
        """About the code , the script search some information"""
        req = requests.get(f"https://fr.openfoodfacts.org/api/v0/produit/{code}.json").json()
        data = req["product"]
        sep = "\n#######################################################################################\n"
        print(sep, "Nom du nouveu produit>", data["product_name_fr"], sep, \
              "\nInformation sur ces nutriments:\n", data["nutriments"], sep, \
              "\nLien vers image du produit>", data["image_front_url"], sep, "\nLieu(x) de vente>", data["stores"], sep)
        ex = ""
        while ex != "1":
            choice = input("Voulez vous enregistrer ce produit comme produit principal? o/n: ")
            if choice == "o":
                nam = data["product_name_fr"]
                name = str(nam).strip(",")
                self.changeProduct(name, id)
                ex = "1"
                print(sep)
                print("Le produit a été changé.")
                print(sep)
                input("Taper entrer pour sortir")
            elif choice == "n":
                print(sep)
                print(" \nLe produit n'a pas été changé.\n ")
                print(sep)
                ex = "1"
            else:
                print(" \nJe n'ai pas compris votre demande.\n")
