from lib.laferme import ferme
from lib.TP_2_Mbengue_Mohamed import * 


while True :
    print_menu()
    choix = input("Votre choix")
    if choix == "1":
        print_separator()
        choix-animal()
    elif choix == "2":
        ferme.crier()
    elif choix == "3":
        if farm_is_empty():
            continue
        print_separator()
        nom = input("Nom de l'animal a tuer: \\t")
        while nom not in ferme.animal.key() and nom != "q":
            print("Cet animal n'existe pas")
            nom = input("Nom de l'animal à tuer: \\t")
        tuer_animal(nom)
    elif choix == "4":
        print(str(ferme))
    elif choix == "5":
        break
