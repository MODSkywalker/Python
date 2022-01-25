# LISTE

# Pour tranformer une chaîne de caractère en liste, on utilise la méthode "split"
# Par défaut, lorsqu'on ne passe aucun caratère en argument, la méthode fractionne pour les espaces
# Cette méthode n'écrase pas la variable dans laquelle elle est contenu
# Il faut donc la stocker dans une varirable
# Si on écrase le contenu de la variable initiale, on transforme la chaîne de caractère en liste
# Si on l'utilise sur un caractère qui n'est pas présent dans la chaîne de caractère, 
# On obtient quand-même une liste qui ne contiendra cependant q'un seul élément
courses = "Riz, Pommes, Lait, Salade, Saumon, Beurre"
courses_liste = courses.split(", ")
print(courses)
print(courses_liste)