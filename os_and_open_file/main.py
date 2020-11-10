# coding: utf-8

import os

# get the user name (ex: PYTHON for the via computer)
nomUtilisateur = os.getlogin()

file = open("C:/users/"+ nomUtilisateur + "/Desktop/read.me.txt", "r")
content = file.read()
print(content)
