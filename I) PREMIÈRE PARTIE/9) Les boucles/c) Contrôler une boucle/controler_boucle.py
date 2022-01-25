# LES BOUCLES

# Les instructions qui nous permettent de contrôler le déroulement d'une boucle sont:
# 'contine' et 'break'

# Lorsqu'une boucle for ou while rencontre l'instruction 'continue', elle passe à la prochaine itération
# Sans exécuter le reste du code qui se trouve après
liste = ["1", "4", "25", "Paul", "3", "Pierre"]
for element in liste:
    if element.isdigit():
        continue
    print(element)

# Lorsqu'une boucle for ou while rencontre l'instruction 'break', elle sort définitivement de la boucle
# Et sans exécuter le reste du code qui se trouve après
liste = ["1", "4", "25", "Paul", "3", "Pierre"]
for element in liste:
    if element.isdigit():
        break
    print(element)