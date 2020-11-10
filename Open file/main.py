# coding: utf-8

def open_file(file_to_open):
    """
        open file, save content and modify the file
    """
    # ouvrir le fichier texte en mode lecture 'r'
    file = open(f"Open file/{file_to_open}.txt", 'r')
    # récupérer le contenu du fichier ouvert
    content = file.read()
    # créer une liste avec les mots du contenu
    list_words = content.split()
    # fermer le fichier
    file.close()
    # ouvrir le fichier pour le modifier
    file = open(f"Open file/{file_to_open}.txt", 'w')
    # écrire chaque mot sur une ligne
    for word in list_words:
        file.write(word+"\n")
    # fermer le fichier
    file.close()
    return list_words

if __name__ == "__main__":
    print(open_file("my_file"))
    # regarder le fichier qui est dans vsc pour voir les mots sur chaque ligne

#! récupérer les lignes d'un fichier
#! list_line = file.readlines()    Pour lecture
#! file.writelines(list_lines)   Pour modifier / écrire / écraser chaque élémént sur une ligne



## this code works, but no argument
# def open_file():
#     # ouvrir le fichier texte en mode lecture 'r'
#     file = open("Open file/my_file.txt", 'r')
#     # récupérer le contenu du fichier ouvert
#     content = file.read()
#     # créer une liste avec les mots du contenu
#     list_words = content.split()
#     # fermer le fichier
#     file.close()
#     return list_words


# if __name__ == "__main__":
#     print(open_file())

