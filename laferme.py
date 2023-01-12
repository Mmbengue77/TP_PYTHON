class Animal ():
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    def cri (self):
        print("Cri de l'animal")


class ferme:
    def _init_(self):
        self.animal = {}
       # self.animaux[animal.nom] = animal
    def ajouter_animal(self, animal):
        self.animaux[animal.nom] = animal
    def tuer_animal(self, nom):
        del self.animal[nom]
    def get_animal(self, nom):
        return self.animaux[nom]
    def ajouter_lapin(nom, age):
         input ("Nom: ")
         input ("Age: ")
         return Lapin(nom, age)
    def crier(self):
        for animal in self.animaux.items():
            animal[1].cri()