import csv


csvfile = 'persons.csv'

def creer():
   
    with open("persons.csv", mode='a', newline="") as csvFile:
        fieldNames = ['Nom', 'Prenom', 'Age', 'Ville']
        # writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames)
        Nom = input("Nom : ")
        Prenom = input("Prenom : ")
        Age = input("Age : ")
        Ville = input("Ville : ")
        writer.writerow({'Nom' : Nom, 'Prenom': Prenom, 'Age': Age, 'Ville' : Ville})
        print("Vous etes inscrit")
        show_menu()

def Supprimer():
    global matriculadel 
    contacts = []
    with open(csvfile, mode="r", newline="") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        for row in csvReader:
            contacts.append(row)
    print(f'Nom \t Prenom \t Age \t Ville \t' )
    for data in contacts:
        print(f"{data['Nom']} \t {data['Prenom']} \t {data['Age']} \t {data['Ville']}")
    print("-")
    matriculadel = input("Supprimer Nom :")
    index = 0
    for data in contacts:
        if data['Nom'] == matriculadel:
            contacts.remove(contacts[index])
        index = index + 1
    with open(csvfile, mode="w", newline="") as csvFile:
        fieldNames = ['Nom', 'Prenom', 'Age', 'Ville']
        writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
        writer.writeheader()
        for newData in contacts:
            writer.writerow({'Nom': newData['Nom'], 'Prenom': newData['Prenom'], 'Age': newData['Age'], 'Ville': newData['Ville']})

def Modifier():
    contacts = []
    with open("persons.csv", mode='r', newline="") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        print(type(csvReader))
        for row in csvReader:
            contacts.append(row)
        print(list(contacts))
    print(f'Nom \t\t Prenom \t\t Age \t\t Ville \t\t')

    for data in contacts:
        print(f"{data[0]} \t\t {data[1]} \t\t {data[2]} \t\t {data[3]}")
    
    Nom = input("Nom : ")
    for data in contacts:
        if data[0] == Nom:
            print(f"""Voici {data[0]},{data[1]},{data[2]},{data[3]}
            Voulez vous le modifier?
            1.Modifier
            2.Continuer""")
            choix = input("Faites un choix :")
            while choix not in {"1", "2"}:
                if choix not in {"1", "2"}:
                    print("Rentrez 1 ou 2")
                    choix = input()
                elif choix == '1':
                    data[1] = Prenom
                    data[3]= Ville
                elif choix == "2":
                    continue
                show_menu

    
    Prenom = input("Nouveau Prenom : ")
    Ville = input("Nouvelle Ville : ")
    index = 0
    show_menu
             
    with open('persons.csv', 'w') as f:
        for data in contacts:
            f.write(f"{data[0]},{data[1]},{data[2]},{data[3]}\n")
    show_menu


        
       
    
      
def Afficher ():

    with open("persons.csv", mode='a', newline="") as csvFile:
        f = open("persons.csv", "r")
        #ligne = f.readline()
        contenu = f.read()
        print(contenu)
        f.close()
        print("Information Enregistrées")
    show_menu

       # fieldNames = ['Nom', 'Prenom', 'Ville']
       # writer = csv.DictWriter(csvFile, fieldnames=fieldNames, delimiter=',')
       # matricula = input("Matricula : ")
       # curso = input("Curso : ")
       # email = input("E-MAIL : ")
        #writer.writerow({'MATRICULA' : matricula, 'CURSO' : curso, 'EMAIL': email})
        #print("Information Enregistrées")


    with open("persons.csv", mode='r', newline="") as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Nom', 'Prenom', 'Age', 'Ville'])
        filewriter.writerow(['Mbengue', 'Mohamed', '26', 'Torcy'])
        filewriter.writerow(['Cisse', 'Mame Seny', '25', 'Defense'])
        filewriter.writerow(['Diallo', 'Fatoumata', '55', 'Conakry'])
        filewriter.writerow(['Mbengue', 'Omar', '20', 'Dakar'])
        filewriter.writerow(['Mbengue', 'Mohamed Seny', '5', 'Lagny'])


        reader = csv.reader(csvfile)

        #read file row by row
        for row in reader:
            print (row)


def show_menu():
    print(f'''================ Personnel ================
[1] Afficher la liste
[2] Creer une Personne
[3] Supprimer une Personne
[4] Modifier une Personne
[0] Sair
=======================================''')
    selected_menu = input("Choisir une option => ")

    if selected_menu == "1":
        return Afficher()
    elif selected_menu == "2" :
        return creer()
    elif selected_menu == "3":
        return Supprimer(),
    elif selected_menu == "4":
        return Modifier()
    elif selected_menu == "0":
        return exit()
    else:
        print("Alternative invalide!!!")
    show_menu()

def back_to_menu():
    input("\nPresse ENTER ALTERNATIVA INVALIDA")
    show_menu()

