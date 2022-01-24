# inverser le mot
mot = input("Saisissez le mot que vous souhaiter inverser : ")
for i in reversed(mot):
    print(i)

# Ou
for lettre in mot[::-1]:
    print(lettre)