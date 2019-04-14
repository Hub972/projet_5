# usr/bin/python3
# -*- coding: utf-8 -*-


from requests_off_.requests_off import Request
from choice_.choice import Choice
import sys

from db.db_interaction import Interaction
from db.db_engine import Products


class Run:
    def __init__(self):
        self.req = Request() # for the request with the API
        self.choice = Choice() # for the different choice in the script
        self.interaction = Interaction() # for transaction with the data base

    def lunch(self):
        """The synergy to control the script """
        qut1 = ""
        shutdown = ""
        while shutdown != "q": # for quit the script
            inner = self.choice.baseChoice()
            qut = ""
            while qut != "q": # for return in the first choice
                if inner == "1":
                    cat = ""
                    cat = self.choice.chooseCat()
                    if cat == "00":
                        break
                    while qut1 != "q": # for return to the category choice
                        qut1 = self.interaction.displayTable(Products, cat, 0)
                        if qut1 == "q":
                            qut1 = ""
                            break
                        try:
                            code, id = self.choice.chooseSubtitute(Products, qut1)
                            name = self.req.searchProductCode(code) # request with the api
                            self.choice.choiceProduct(name, id)
                        except UnboundLocalError:
                            print("Produit inconnue...")
                elif inner == "2": # display the substitute products
                    all_cat = int()
                    self.interaction.displayTable(Products, all_cat, 1) # display the substitutes products
                    qut = "q"
                elif inner == "00":
                    shutdown = "q"
                    print("##########################################")
                    print("Merci et à bientôt.")
                    input("##########################################")
                    sys.exit(0)
                else:
                    self.choice.badChoice()
                    qut = "q"
