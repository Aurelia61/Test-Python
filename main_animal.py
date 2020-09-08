# coding: utf-8

import psycopg2    # librairie pour ouvrir la bdd

animals = []


def main():
    """
        Program entry
    """

   # * connect to DB (database)
    MyConnection = None
    
    try :
        MyConnection = psycopg2.connect(    
        host = "localhost",          # serveur de base de données (ou adresse IP du serveur) ici en local sur l'ordi     
        database ="dojo_animal",     # le nom de la bdd
        user = "postgres",
        password = "Formation2020-at"
    )
    except(Exception, psycopg2.DatabaseError) as Error:
        #error
        print("not connecting")    # ! pas le bon texte entre ""

    # * try DB
    if MyConnection is not None:
        # * first query to test DB
        MyCursor = MyConnection.cursor()    # ouvrir un curseur
        MyQuery = "SELECT version()"     # ouvrir une requete
        MyCursor;execute(MyQuery)
        MyResult = MyCursor.fetchone()       # fetchall si plusieurs résultats
        # * print query result
        print(MyResult)   #! pas le bon texte

        # * close ressources
        MyCursor.close()
        MyConnection.close()

    




if __name__ == "__main__":
    main()