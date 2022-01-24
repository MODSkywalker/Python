# Remplacer des boucles par des compréhensions de listes
 
# nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
# nombres_pairs = []
# for i in nombres:
#     if i % 2 == 0:
#         nombres_pairs.append(i)

# print(nombres_pairs)

nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres if i % 2 == 0]


print(nombres_pairs)

# ---------------------------------------------------- #

# nombres = range(-10, 10)
# nombres_positifs = []
# for i in nombres:
#     if i >= 0:
#         nombres_positifs.append(i)

# print(nombres_positifs)

nombres = range(-10, 10)
nombres_positifs = [i for i in nombres if i >= 0]

print(nombres_positifs)

# ---------------------------------------------------- #

# nombres = range(5)
# nombres_doubles = []
# for i in nombres:
#     nombres_doubles.append(i * 2)

# print(nombres_doubles)

nombres = range(5)
nombres_doubles = [i*2 for i in nombres]

print(nombres_doubles)

# ---------------------------------------------------- #

# nombres = range(10)
# nombres_inverses = []
# for i in nombres:
#     if i % 2 == 0:
#         nombres_inverses.append(i)
#     else:
#         nombres_inverses.append(-i)

# print(nombres_inverses)

nombres = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]

print(nombres_inverses)