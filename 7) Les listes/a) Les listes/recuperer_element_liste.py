# LES LISTES

# Pour récupérer un élément d'une liste on utilise ce qu'on appelle l'indice du dit élément dans la liste
# Un indice n'est autre que la position d'un élément dans une structure de données
# En Python comme dans de nombreux langages informatique l'indice commence à ZERO "0"
langage = ["C", "HTML", "CSS", "Java", "Python"]
for i in range(5):
    print(langage[i])

# En Python il est possible d'utiliser un indice négatif nous permettant de commencer par la fin de la liste
# Ainsi l'indice "-1" nous retournera toujours le dernier élément de la liste peut importe sa taille
print("Le dernier élément de la liste est : " + langage[-1])