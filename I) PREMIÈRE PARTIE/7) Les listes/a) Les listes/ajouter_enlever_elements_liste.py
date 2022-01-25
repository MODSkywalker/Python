# LES LISTES

# Pour ajouter des éléments à une liste, on utilise la méthode "append()"
# Cette méthode ne permet d'ajouter qu'une seule valeur à la fois
villes = ["Bamako", "Segou", "Kidal"]
villes.append("Sikasso")
print(villes)

# Pour ajouter plusieurs éléments d'un coup on utilise la méthode "extend([])" 
villes.extend(["Kayes", "Tombouctou", "Mopti"])
print(villes)

# Pour enlever un élément de notre liste on utilise la méthode "remove()"
# Cette méthode ne supprimera que la première occurence du chiffre ou du mot passé en argument
# S'il en existe 3 il faudra faire appel à la méthode 3 fois ! 
villes.remove("Kayes")
print(villes) 