# coding: utf-8

class Rectangle:

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        return 2*(self.longueur+self.largeur)

    def surface(self):
        return self.longueur*self.largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        # long et larg sont hérités de la classe rectangle
        Rectangle.__init__(self, longueur, largeur) 
        # attribut propre au parallelepipede
        self.hauteur = hauteur
    
    def volume(self):
        return self.longueur*self.largeur*self.hauteur


if __name__ == "__main__":
    #! instanciation d'un rectangle
    mon_rectangle = Rectangle(7,5)
    #! test
    print(f"\nLongueur : {mon_rectangle.longueur}")
    print(f"Largeur : {mon_rectangle.largeur}\n")
    print(f"Surface : {mon_rectangle.surface()}\n")
    print(f"Perimetre : {mon_rectangle.perimetre()}\n")

    #! instanciation d'un parallelepipede
    mon_para = Parallelepipede(8,5,3)
    print(f"Volume du para: {mon_para.volume()}\n")
    print(f"Surface rect : {mon_para.surface()}\n")


