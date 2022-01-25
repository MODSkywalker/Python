# Le but de cet exercice est de modifier le script afin d'afficher l'index de chaque lettre du mot 'Python'.
# Pour l'instant le script retourne une erreur. À vous de la corriger. Votre script doit donc afficher :
# 0
# 1
# 2
# 3
# 4
# 5
# Petite astuce : vous allez devoir utiliser une fonction qui permet de récupérer la longueur d'un élément...
# mot = "Python"

# for i in range(mot):
#     print(i)

mot = "Python"
# Pour pouvoir itérer sur la longueur d'une chaîne de caractère on utilise la fonction 'len' pour récupérer sa longueur
for i in range(len(mot)):
    print(i)