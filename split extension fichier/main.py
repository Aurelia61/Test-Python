# coding: utf-8

fichier = input("Nom du fichier avec son extension :")

# séparer la string au niveau des " . "  ( ! donne une liste sans le point)
liste_fichier = fichier.split(".")

print(liste_fichier)

extension = liste_fichier[-1]
print(f"Extension : {extension}")