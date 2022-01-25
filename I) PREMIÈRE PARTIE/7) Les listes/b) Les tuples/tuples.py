# LES TUPLES

# Les tuples, c'est quasiment la même chose que les listes.
# La différence principale, c'est qu'on ne peut ni ajouter ni enlever d'éléments à un tuple.
# On utilise les tuples pour des questions de rapidité.
# Comparé aux listes, les tuples sont restreints en termes de fonctionnalités
# Ils prennent ainsi moins de place dans la mémoire

# Pour définir un tuple, la syntaxe est similaire aux listes sauf qu'on utilise les parenthèses au lieu des crochets :
mon_tuple = (1, 2, 3, 4, 5)
print(mon_tuple)

# Comme les listes, un tuple peut contenir des éléments de différents types :
mon_tuple = (250, "Python", True)
print(mon_tuple)

# Il est possible de convertir un tuple en liste et vice-versa grâce aux fonctions "list" et "tuple" :
# Conversion d'un tuple en liste
mon_tuple = (1, 2, 3)
liste = list(mon_tuple)
print(mon_tuple)
# Conversion d'une liste en tuple
mon_tuple = tuple(liste)
print(mon_tuple)