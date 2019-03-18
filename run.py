# usr/bin/python3
# -*- coding: utf-8 -*-


from requests_off import Request
from choice import Choice
import sys

from db.db_interaction import Interaction
from db.db_engine import Products


class Run:
    def __init__(self):
        self.req = Request()
        self.choice = Choice()
        self.interaction = Interaction()

    def lunch(self):
        """The synergy for control the script """
        qut1 = ""
        shutdown = ""
        while shutdown != "q":
            inner = self.choice.baseChoice()
            qut = ""
            while qut != "q":
                if inner == "1":
                    cat = ""
                    cat = self.choice.chooseCat()
                    if cat == "00":
                        break
                    while qut1 != "q":
                        qut1 = self.interaction.displayTable(Products, cat, 0)
                        if qut1 == "q":
                            qut1 = ""
                            break
                        try:
                            code, id = self.choice.chooseSubtitute(Products, qut1)
                            self.req.searchProductCode(code, id)
                        except UnboundLocalError:
                            print("Produit inconnue...")
                elif inner == "2":
                    all_cat = int()
                    self.interaction.displayTable(Products, all_cat, 1)
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
