# LES BOUCLES

# La fonction 'any()' permet de vérifier si au moins un élément de la liste est vrai
# Si au moins un élément de la liste est vraie cette fonction retourne "True"
from importlib.metadata import files


liste_1 = [False, False, True, False]
test_1 = any(liste_1)
print(test_1)

# La fonction 'all()' permet de vérifier si tous les éléments de la liste sont vrais
# Si tous les éléments de la liste sont vrais cette fonction retourne "True"
liste_2 = [True, False, True, False]
test_2 = all(liste_2)
print(test_2)

files = "C:/Users/moha/images"
all([f.endswith(".jpg") for f in files])