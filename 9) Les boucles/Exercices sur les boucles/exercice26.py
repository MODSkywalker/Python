# Récupérer seulement les nombres pairs
# Dans cet exercice, nous avons une liste qui contient 50 nombres.
# Le but de cet exercice est de récupérer dans la liste nombres_pairs, uniquement les nombres pairs de la première liste :
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

# nombres = range(51)
# nombres_pairs = []

nombres = range(51)
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)