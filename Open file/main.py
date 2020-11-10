# coding: utf-8

def open_file(file_to_open):
    # ouvrir le fichier texte en mode lecture 'r'
    file = open(f"Open file/{file_to_open}.txt", 'r')
    # récupérer le contenu du fichier ouvert
    content = file.read()
    # créer une liste avec les mots du contenu
    list_words = content.split()
    # fermer le fichier
    file.close()
    return list_words


if __name__ == "__main__":
    print(open_file("my_file"))


    
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

