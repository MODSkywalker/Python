# LISTE

# Les listes imbriquées sont des listes à l'intérieur d'une liste
liste = ["Python", ["Java", "C++", ["C"]], ["Ruby"]]

# On va afficher la chaîne de caractère "Java" contenu dans la première liste imbriquée dans notre liste
print(liste[1][0])

# On va afficher la chaîne de caractère "C" contenu dans la liste imbriquée dans la première liste imbriquée de notre liste
print(liste[1][-1][0])