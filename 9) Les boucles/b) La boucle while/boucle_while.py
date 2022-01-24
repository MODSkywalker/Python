# LES BOUCLES

# La boucle while
i = 0
while i < 5:
    print("Bonjour")
    i += 1  # i++

# La boucle hile est surtout utiliser lorsqu'on a aucune idée du nombre d'itération de la boucle
continuer = "o"
while continuer == "o":
    print("On continue ...")
    continuer = input("Voulez-vous continuer ? o/n: ")

# Pour une boucle while infini à coup sûr on utilise le boolean "True"
# Le seule moyen de sortir de cette boucle est d'arrêté le processus dans le gestionnaire des tâches
# Avec le module "time" permet d'éxecuter l'opération après un nombre de temps
# N.B: La durée de temps est évaluée en séconde "s"
import time
while True:
    print("Sauvegarde en cours...")
    time.sleep(600)