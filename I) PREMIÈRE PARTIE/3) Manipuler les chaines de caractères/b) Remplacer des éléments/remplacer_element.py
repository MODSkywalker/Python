# Remplacer un ou plusieurs chaîne(s) de caractères par un autre: replace()
a = "bonjour".replace("jour", "soir")
print(a)

# Enlever des éléments dans une chaîne de caractères: strip()
# Par default elle enlève les espaces
b = "  bonjour  ".strip()
print(b)
# Cette méthope supprime les caractères passés en arguments sans se soucier de l'ordre
b = "  bonjour  ".strip(" ujor")
print(b)
# Les sous-méthodes:
# rstrip(): supprime les caractères passés en argument se trouvants à droite de la chaîne de caractères
b = "  bonjour  ".rstrip(" ujor")
print(b)
# Les sous-méthodes:
# lstrip(): supprime les caractères passés en argument se trouvants à gauche de la chaîne de caractères
b = "  bonjour  ".lstrip(" ujor")
print(b)