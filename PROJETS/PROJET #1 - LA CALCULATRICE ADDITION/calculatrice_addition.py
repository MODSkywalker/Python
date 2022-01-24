# Demander à l'utilisateur de saisir deux nombres
# Les additionner
# Puis afficher le résultat

a = input("Veillez entrer un premier nombre: ")
b = input("Veillez entrer un deuxième nombre: ")

# Avec la méthode f-string()
resultat = f"Le résultat de l'addition du nombre {a} avec le nombre {b} est égal à {int(a)+int(b)}"
print(resultat)

# Avec la méthode format()
resultat = "Le résultat de l'addition du nombre {x} avec le nombre {y} est égal à {somme}".format(x=a, y=b, somme=int(a)+int(b))
print(resultat)