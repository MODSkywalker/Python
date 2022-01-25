# Les opérateurs logiques sont: or, and et not
# or = ou
# and = et
# not = pas

# NB: "and" > "or". Par defaut AND est prioritaire sur OR en python.
5 > 2 and 5 < 10 or 5 > 15
# Pour lever cette priorité on utilise des parenthèses
5 > 2 and (5 < 10 or 5 > 15)

# "not" retourne l'inverse de ce qu'on lui donne
user = "Dark_Vador"
if not user == "Skywalker":
    print("Accès refusé !")