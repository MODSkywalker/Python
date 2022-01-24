# Dans cet exercice, vous devez générer deux nombres aléatoires et indiquer à l'utilisateur lequel des deux nombres est le plus grand.
# Par exemple :
# Un nombre a est généré aléatoirement et prend la valeur de 15.
# Un nombre b est généré aléatoirement et prend la valeur de 26.
# Votre script doit afficher la phrase suivante :
# "Le nombre b est plus grand que le nombre a."
# Dans le cas contraire, le script devra afficher :
# "Le nombre a est plus grand que le nombre b."
# Si les nombres sont égaux, le script devra afficher :
# "Le nombre a et le nombre b sont égaux."
# 
# Les deux nombres générés aléatoirement peuvent être des nombres entier ou des nombres décimaux, 
# cela n'a pas d'importance. Vous pouvez également choisir n'importe quel intervalle pour générer 
# votre nombre aléatoire.
# Attention, il est bien important que vous affichiez ces phrases précisément. Pour valider l'exercice, 
# votre script doit afficher l'une ou l'autre des phrases ci-dessus. Si vous oubliez le point à la fin 
# de la phrase ou la majuscule par exemple, l'exercice ne sera pas validé ! Aussi, vous ne devez pas 
# afficher les valeurs des nombres a et b mais bien la lettre a et la lettre b (pas besoin de concaténer 
# les variables a et b dans la phrase donc !).

# Importation de la méthode random
import random

# Affectation des deux nombres aléatoires
a = random.randint(0, 2000)
b = random.randint(50, 500)

# Comparaison des nombre
if a > b :
    print(f"Le nombre {a} est plus grand que le nombre {b}.")
elif a < b :
    print(f"Le nombre {b} est plus grand que le nombre {a}.")
else :
    print(f"Le nombre {a} et le nombre {b} sont égaux.")