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


