from ctypes.wintypes import BOOLEAN
from email import message
import sys
import random
import emoji

# Règles du jeu
# Le but de ce projet est de créer un jeu de rôle textuel dans le terminal.
#     Le jeu comporte deux joueurs : vous et un ennemi.
#     Vous commencez tous les deux avec 50 points de vie.
#     Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie.
#     L'ennemi ne dispose d'aucune potion.
#     Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.
#     Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.
#     L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.
#     Lorsque vous utilisez une potion, vous passez le prochain tour.

# Joueurs: l'utilisateur et le CPU
user = input("Pseudonyme: ")
cpu = "CPU"
# Les point de vie: HP
hp_user = 50
hp_cpu = 50
# La liste de potion
potion_hp = ["potion_hp_1", "potion_hp_2", "potion_hp_3"]
# Initialisation de la liste de potion à des valeurs aléatoires entre [15,50]
for i in range(3):
    potion_hp[i] = random.randint(15, 50)
# Message menu
MENU = "Souhaitez-vous : Attaquer (1) ou Utiliser une potion (2) ? : "
# Le de l'utilisateur
option = 0
# initialisation du tour
tour = True

FIN = "Fin du jeu."

while not (hp_cpu == 0 or hp_user == 0):
    # Initialisation aléatoire des attaques
    att_user = random.randint(5, 10)
    att_cpu = random.randint(5, 15)

    # Le tour suivant le choix de l'option 2
    if tour == False:
        print("Vous passez votre tour...")
        hp_user -= att_cpu
        print("L'ennemi vous a infligé 8 point de dégats ⚔️")
        print(f"Il vous reste {hp_user} point de vie.")
        print(f"Il reste à l'ennemi {hp_cpu} point de vie.")
        print("------------------------------------------------------")
        tour = True
        continue
    
    if tour == True:
        # Initialisation du choix des options de l'utilisateur
        option = input(MENU)
        # l'option utilisateur n'est pas un nombre
        if not option.isdigit():
            option = input(MENU)
            continue
        # Si l'option saisie est un nombre différent de 1 et 2
        option = int(option)
        if not (option == 1 or option == 2):
            print("Votre choix n'est pas valide...")
            continue
        
        # L'utilisateur choisi d'attaquer
        if option == 1:
            # S'il ne reste plus assez de HP au CPU
            if att_user > hp_cpu:
                att_user = hp_cpu
            # Soustraction des points d'attaque de l'utilisateur aux HP du CPU
            hp_cpu -= att_user
            print(f"Vous avez infligé {att_user} points de dégats à l'ennemi ⚔️")
        # L'utilisateur choisi de prendre une potion
        else:
            # Plus de potion
            if not potion_hp:
                print("Vous n'avez plus de potions...")
                continue
            # Lorsqu'il reste encore des potions
            else:
                # Initialisation du prochain tour de l'utilisateur à False pour qu'il ne puisse pas jouer
                tour = False
                # Ajout de la valeur de la potion à celle du HP de l'utilisateur
                hp_user += potion_hp[0]
                # On supprime la potion utilisée de la liste et on la récupère dans une nouvelle variable
                last_option_used = potion_hp.pop(0)
                # Affichage de la valeur de points de HP récupérer 
                print(f"Vous récupérez {last_option_used} points de vie" + emoji.emojize(" :red_heart:  ") + f"({len(potion_hp)} restante(s))")
        # Le tour du CPU
        # S'il ne reste plus assez de HP à l'utilisateur
        if att_cpu > hp_user:
            att_cpu = hp_user
        # Soustraction des points d'attaque du CPU aux HP de l'utilisateur
        hp_user -= att_cpu
        # Affichage des points 
        print(f"L'ennemi vous a infligé {att_cpu} point de dégats ⚔️")
        print(f"Il vous reste {hp_user} point de vie.")
        print(f"Il reste à l'ennemi {hp_cpu} point de vie.")
        print("------------------------------------------------------")

# Fin de partie
if hp_cpu == 0:
    print("Tu as gagné ! 💪")
    print(FIN)
else:
    print("Dommage, vous avez perdu !")
    print(FIN)