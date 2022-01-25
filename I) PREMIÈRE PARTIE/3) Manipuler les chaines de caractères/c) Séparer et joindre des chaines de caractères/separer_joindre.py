# Pour séparer une chaîne de caractères sur les caractères passés en argument on utilise la fonction: split()
# Cette méthode retourne une liste
a = "1, 2, 3, 4, 5".split(", ")
print(a)

# Pour joindre avec le caractère spécifié tous les éléments d'un itérable passé en argument on utilise la fonction: join()
b = ", ".join("1, 2, 3, 4, 5".split(", "))
print(b)