# LES LSITES

# Pour récupérer certains éléments de la liste on utilise ce qu'on appelle les "slices" ou tranches
# Le slice exclusif "[a, b["
liste = ["Utilisateur_01", "Utilisateur_02", "Utilisateur_03", "Utilisateur_04", "Utilisateur_05", "Utilisateur_06",]

# Affichons uniquement le premier élément de la liste
print(liste[0:1])
# Pour récupérer les deux premier éléments on va jusqu'à l'index 2
print(liste[0:2])

# Pour récupérer le dernier élément on ne spécifie d'index à la fin de l'intervalle
# Pour récupérer la liste entière on procède ainsi:
print(liste[:])

# Pour récupérer un utilisateur sur 2 en allant jusqu'à la fin on procède ainsi
print(liste[::2])
# Récupérer les éléments de la liste en commençant par le 2ème élement de la liste 3éme élément de la liste avec un pas de 2
print(liste[1:3:2])

# Pour inverser l'ordre d'une liste avec un "slice"
print(liste[::-1])