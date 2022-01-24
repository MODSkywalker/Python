# LES BOUCLES

# En Python il est possible de faire un boucle for/else
# Si on parcours tous éléments de la liste san jamais rencontrer l'instruction 'break'
# On passe dans le 'else'
prenoms = ["Pierre", "Jean", "Marc"]
for prenom in prenoms:
    if prenom == "Patrick":
        print("Patrick a été trouvé !")
        break
else:
    print("Partick est introuvable...")