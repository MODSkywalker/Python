# Ordonner une chaîne de  caractères
# Le but de cet exercice et de remettre en ordre alphabétique les prénoms présents dans la chaîne de caractère.
# Vous devez créer une variable chaine_en_ordre qui, à la fin de l'exercice, doit contenir la chaîne de caractère suivante :
# "Anne, Julien, Lucien, Marie, Pierre"
chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine_liste = chaine.split(", ")
chaine_liste.sort()
chaine_en_ordre = ", ".join(chaine_liste)
print(chaine_en_ordre)