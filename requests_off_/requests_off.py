# usr/bin/python3
# -*- coding: utf-8 -*-


import requests


class ApiRequest:

    @staticmethod
    def searchProductCode(code):
        """About the bar code , the script search some information in the 'openfoodfacts' API"""
        res = requests.get(f"https://fr.openfoodfacts.org/api/v0/produit/{code}.json").json()
        data = res["product"]
        return data
    @staticmethod
    def displayInfoProduct(data):
        sep = "#"*87
        sep = "\n"+ sep +"\n"
        print(sep, "Nom du nouveu produit>", data["product_name_fr"], sep, \
              "\nInformation sur ces nutriments:\n", data["nutriments"], sep, \
              "\nLien vers image du produit>", data["image_front_url"], sep, "\nLieu(x) de vente>", data["stores"], sep)
        name_d = data["product_name_fr"]
        name = str(name_d).strip(",")
        return name

