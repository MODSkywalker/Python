# La méthode format() nous évite d'utiliser la conversiont de variables

age = 26
phrase = "J'ai {} ans".format(age)
print(phrase)

# Cela peut s'écrire comme ça également
phrase = "J'ai {x} ans".format(x=age)
print(phrase)

# On peut passer plusieurs variables en arguments
age_2 = 27
phrase = "J'ai {} ans, bientôt {} !".format(age, age_2)
print(phrase)

# Utiliser la même variable plusisieurs fois
phrase = "J'ai {0} ans, oui {0} !".format(age)
print(phrase)