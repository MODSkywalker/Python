# LES LISTES

# Les opérateurs d'appartenance vérifie si un élémént appartient à la liste ou pas
# Ils sont au nombre de deux :
# "in" : Renvoie 'true' si l'élément appartient à la liste, 'false' sinon
# "not in" : Renvoie 'true' si l'élément n'appartient pas à la liste, 'false' sinon
utilisateurs = ["Paul", "Pierre", "Marie"]
# Avec la structure conditionnelle ci-dessous nous pouvons utiliser la méthose remove sans crainte de message d'erreur à la compilation
if "Paul" in utilisateurs:
    utilisateurs.remove("Paul")
