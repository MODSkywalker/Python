# Certains objets sont ce qu'on appelle des objets "callables" c'est à dire appellables
# C'est ce qu'on appelle des "fonctions"
# Les modules ne sont pas "callable"
import pprint
print(callable(pprint))
if callable(pprint):
    print("pprint une fonction dans ce cas de figure. Il est donc callable !\n")
else:
    print("pprint un module dans ce cas de figure. Il n'est donc callable !\n")

# En important la fonction "pprint" depuis le module pprint, on peut 
from pprint import pprint
print(callable(pprint))
if callable(pprint):
    print("\"pprint\" une fonction dans ce cas de figure. Il est donc callable !\n")
else:
    print("\"pprint\" un module dans ce cas de figure. Il n'est donc callable !\n")


# Certaines fonctionnalités des modules sont des attributs
# Ils ne sont pas callables
# On les confond facilement avec les fonctions
import os
pprint(dir(os))
# Choissisons dans cette liste "name".
# # A première vu, on peut croire que "name" est une fonction de la methode "os".
# Mais "name" est un attribut de la méthode "os" et non une fonction
# os.name permet d'afficher le nom du système d'exploitation sur lequel on travail
print(os.name)

if callable(os.name):
    print("\"os.name\" une fonction du module \"os\". Il est donc callable !\n")
else:
    print("\"os.name\" un attribut du module \"os\". Il n'est donc pas callable !\n")
