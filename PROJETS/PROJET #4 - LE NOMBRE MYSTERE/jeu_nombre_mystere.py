# LE JEU DU NOMBRE MYSTERE
import random

print("*** Le jeu du nombre mystère ***")
mysterious_number = random.randint(0, 100)
essai = 5
n = 0

while essai > 0:
    # Affichage du nombre d'esai restant   
    print(f"Il te reste {essai} essais")

    # Récupération de la saisie de l'utilisateur
    user_number = input("Devine le nombre mystère: ")
    # Teste si la valeur saisie est numérique
    if not user_number.isdigit():
        print("Veillez entrer un nombre valide.")
        continue
    # Convertion du nombre saisi en integer
    user_number = int(user_number)
    
    # La valeur saisie est plus petite que celle du nombre mystère
    if mysterious_number < user_number:
        print(f"Le nombre mystère est plus petit que {user_number}")
    # La valeur saisie est plus grande celle du nombre mystère
    elif mysterious_number > user_number:
        print(f"Le nombre mystère est plus grand que {user_number}")
    else:
        break
    # Réduction du nombre d'eesai
    essai -= 1
    # Nombre de tentative effectué pour trouver le nombre mystère
    n += 1

# Gagné ou perdu
if essai == 0:
    print(f"Dommage ! Le nombre mystère était {mysterious_number}")
else:    
    print(f"Bravo ! Le nombre mystère était bien {mysterious_number} !\nTu as trouvé le nombre mystère en {n} essai")

# Message de fin de partie
print("Fin du jeu.")