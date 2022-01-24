# LA LISTE DE COURSE V1.0
import sys
import emoji

# Initialisation de la liste
liste = []

# Creation des options
MENU = """Choisissez parmi les 5 options suivantes : 
1: Ajouter un élément à la liste
2: Retirer un élément à la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
"""

# Liste d'option
MENU_CHOIX = ["1", "2", "3", "4", "5"]

# Boucle sur la liste
while True:
    # Choix utilisateur
    choix = input(MENU)
    if choix not in MENU_CHOIX:
        print("Veiller choisir une option valide...")
        continue
    # Option 1: Ajouter un nouvelle élément à la liste
    if choix == "1":
        nouvel_element = input("Entrer le nom de l'élément à ajouter à la liste : ")
        liste.append(nouvel_element)
    # Option 2: enlever un élément de la liste
    elif choix == "2":
        # Choix de l'élément à enlever
        element_a_enlever = input("Entrer le nom d'un éléméent à retirer de la liste : ")
        # Suppression de tous les éléments de ce nom de la liste
        if element_a_enlever in liste:
            while element_a_enlever in liste:
                liste.remove(element_a_enlever)
            print("L'élément " + element_a_enlever + " a bien été retiré de la liste")
        # Lorsque l'élément que l'on veut supprimer n'est pas dans la liste
        else:
            print("L'élément " + element_a_enlever + " n'est pas présent dans la liste.")
    # Option 3: Afficher la liste
    elif choix == "3":
        for element in liste:
            print(str(liste.index(element)+1) + ". " + element)
    # Option 4: Vider la liste
    elif choix == "4":
        liste.clear()
        if not liste:
            print("Votre liste ne contient plus aucun élément.")
    # Option 5: Quitter la boucle
    elif choix == "5":
        print("A bientôt !")
        sys.exit()