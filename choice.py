# usr/bin/python3
# -*- coding: utf-8 -*-


class Choice:

    def baseChoice(self):
        """Main choice"""
        inner1 = input("Que voulez vous faire?\n1- Remplacer un produit\n2- Voir les \
 produits subtitué\n00- Pour sortir du programme\n>")
        return inner1

    def chooseCat(self):
        """Text for choose a cat"""
        inner1 = ""
        while inner1 != "3" and inner1 != "2" and inner1 != "1" and inner1 != "00":
            inner1 = input("Choisir une catégorie:\n1- Salt products\n2- Sweety products\n3- Liquid products\n00-\
 Pour revenir en arrière: ")
        return inner1


    def badChoice(self):
        """Text for the bad choices"""
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("vous avez fais un mauvais choix ")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
