# usr/bin/python3
# -*- coding: utf-8 -*-
from db.db_interaction import Interaction, Session


class Choice:
    def __init__(self):
        self.interaction = Interaction()
        self.sep = "##########################################"

    def baseChoice(self):
        """Main choice"""
        print(self.sep)
        inner1 = input("Que voulez vous faire?\n1- Remplacer un produit\n2- Voir les \
 produits substitués\n00- Pour sortir du programme\n>")
        return inner1

    def chooseCat(self):
        """Text for choose a cat"""
        inner1 = ""
        while inner1 != "3" and inner1 != "2" and inner1 != "1" and inner1 != "00":
            print(self.sep)
            inner1 = input("Choisissez une catégorie:\n1- Produits salée\n2- Produits sucrée\n3- Produits liquide\n00-\
 Pour revenir en arrière: ")
            if inner1 != "3" and inner1 != "2" and inner1 != "1" and inner1 != "00":
                self.badChoice()
        return inner1

    def badChoice(self):
        """Text for the bad choices"""
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("vous avez fais un mauvais choix ")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    def chooseSubtitute(self, table, l_id):
        """The method take the inner for determinate the product and ask for register"""
        ex = ""
        while ex != "n":
            inner1 = input("\nVeuillez choisir un produit à substituer:\n")
            try:
                if int(inner1) in l_id:
                    dsply_id = self.interaction.session.query(table).filter(table.id == inner1)
                    [print(f"Le produit a subtituer est {pr.name}") for pr in dsply_id]
                    ex = input("Voulez vous changer votre choix? o\\n?:")
                    if ex != "n" and ex != "o": self.badChoice()
                else:
                    self.badChoice()
            except ValueError:
                self.badChoice()
        code = [pr.alter_code for pr in dsply_id]
        for pr in dsply_id:
            id = pr.id
        self.interaction.session = Session()
        return code, id
