# Il existe plusieurs méthodes
# La fonction find()
# Retourne -1 si la chaîne est introuvable
print("--------------- Méthode find() ---------------")
a = "Bonjour le jour".find("jour")
print(a)
b = "Bonjour le jour".find("soir")
print(b)

# La fonction index()
# Retourne Error si la chaîne est introuvable
print("--------------- Méthode index() ---------------")
a = "Bonjour le jour".index("jour")
print(a)
b = "Bonjour le jour".index("soir")
print(b)

# La fonction rfind()
# exactement la même que find mais commence la reparche par la droite
# Il n'existe pas de lfind() car find() par défaut commence à chercher depuis la gauche
print("--------------- Méthode rfind() ---------------")
a = "Bonjour le jour".find("jour")
print(a)