import random

# rangeint est inclusif [x, y]
# Valeur entière entre x et y inclus
r = random.randint(0, 1)
print(r)

# Valeur flottante entre 0 et 1
r = random.uniform(0, 1)
print(r)

# randrange est exclusif [x, y[
# Va récupérer une valeur entre x et y exclus
# On peut lui donner un pas: n
r = random.randrange(0, 101, 10)
print(r)