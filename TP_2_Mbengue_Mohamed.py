from lib.laferme import *

def choix_lapin ():
    nom = input("Nom: ")
    age = input("Age: ")
    print_separator()
    ferme.ajouter_animal(lapin(nom, age))

def choix_oiseau ():
    nom = input("Nom: ")
    age = input("Age: ")
    print_separator()
    ferme.ajouter_animal(oiseau(nom, age))


def print_separator():
    print("                  ")


def choix_animal():
    choix = ""
    while choix not in ("1", "2", "3"):
        print("1. lapin")
        print("2. oiseau")
        print("3. retour")
        choix = input("Choisissez un animal: ")
        if choix =="1":
            choix_lapin
        elif choix == "2":
            choix_oiseau
        elif choix == "3":
            break
        else:
            print("choisir entre 1 ou 2")

def print_menu():
    print_separator()
    print_menu()
    print("Menu")
    print("1 Ajouter un animal")
    print("2 Crie d'un animal")
    print("3 Tuer un animal")
    print("4 Afficher la ferme")
    print("5 Quitter")

def tuer_animal(nom):
    if nom =="q":
        return
    try:
        ferme.tuer_animal(nom)
    except KeyError :
        print(" animal n'existe pas")

def farm_is_empty():
    if ferme.animal == ():
        print_separator()
        print("la ferme est vide")
        return True
    return False
        