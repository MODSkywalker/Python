import random
# "dir" permet de savoir toute les fonctions qu'on peut utiliser avec une méthode
print(dir(random))

# "help" permet d'afficher l'aide d'une fonction en particulier 
# Avec cette dernière nul besoin d'utliser la fonction "print" pour afficher l'aide
help(random.randint)


# La fonction "pprint" permet d'afficher les résultats de la fonction "dir"
# Par ordre alphabétique
# Et une fonction par ligne
# Ce qui est beaucoup plus pratique
# On peut l'utiliser sur pleins de structures de données tels que les "listes"
# Et pleins d'autres
from pprint import pprint
pprint(dir(random))