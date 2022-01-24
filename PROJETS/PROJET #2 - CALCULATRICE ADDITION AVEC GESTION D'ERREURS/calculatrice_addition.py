# Demander à l'utilisateur de saisir deux nombres
# Les additionner
# Puis afficher le résultat

a = input("Veillez entrer un premier nombre: ")
b = input("Veillez entrer un deuxième nombre: ")
while not (a.isdigit() and b.isdigit()):
    # Lorsque c'est uniquement le premier terme qui n'est pas valide
    if a.isdigit():
        b = input("Le deuxième terme n'est pas valide.\nVeillez ressaisir ce nombre: ")
    # Lorsque c'est uniquement le deuxième terme qui n'est pas valide
    elif b.isdigit():
        a = input("Le premier terme n'est pas valide.\nVeillez ressaisir ce nombre: ")
    # Lorsque les deux termes ne sont pas valides
    else:
        print("Veillez entrer deux nombres valides")
        a = input("Veillez entrer un premier nombre: ")
        b = input("Veillez entrer un deuxième nombre: ")

# Avec la méthode f-string()
resultat = f"Le résultat de l'addition du nombre {a} avec le nombre {b} est égal à {int(a)+int(b)}"
print(resultat)

# Avec la méthode format()
resultat = "Le résultat de l'addition du nombre {x} avec le nombre {y} est égal à {somme}".format(x=a, y=b, somme=int(a)+int(b))
print(resultat)