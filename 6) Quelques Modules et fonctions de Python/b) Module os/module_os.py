import os

chemin = "C:/Users/moham/Documents/Udemy/Python"
dossier = os.path.join(chemin, "dossier", "test")
print(dossier)

# Créer un le dossier en question
# makedirs permet de créer un dossier à l'intérieur d'un dossier qui n'a pas encore été créé
# makedirs ne peut pas créer un dossier qui existe déjà
# mkdir permet de créer un dossier qui n'existe pas encore

# os.makedirs(dossier)

# Avant à chaque fois qu'on utilise "makedirs"
# S'assurer que le dossier que l'on souhaite créer n'existe pas déjà 
# Pour se faire il existe deux méthode:
#
# 1ère manière :
if not os.path.exists(dossier):
    os.makedirs(dossier)
# 2ème manière
os.makedirs(dossier, exist_ok = True)

# Supprimer un dossier
# Avant de supprimer un dossier en python il faut toujour s'assurer qu'il existe
# Car on ne peut pas supprimer un dossier qui n'existe pas en Python
if os.path.exists(dossier):
    os.removedirs(dossier)