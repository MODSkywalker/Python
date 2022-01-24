# LES LISTES

# La méthode "index" récupère et renvoie l'index de l'élémént de la liste passé en argument
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
resultat = employes.index("Max")
print(resultat)

# La méthode "count" permet de compter le nombre d'occurence présent dans une liste c-a-d
# Compter le nombre fois que le mot nombre est présent dans la liste
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex", "Max"]
resultat = employes.count("Max")
print(resultat)

# Pour trier une liste par ordre alphabéthique on utilise la méthode "sort"
# Cette méthode est écrase directement la liste à laquelle elle a été appliquée en remplaçant son contenu
# Par la même liste trier par ordre alphabéthique
# Pas besoin de récupérer la liste triée dans une variable
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
employes.sort()
print(resultat)
# On peut par ailleur utiliser la fonction "sorted" qu'on dervra stocker dans une variable
liste_triee = sorted(employes)
print(liste_triee)

# La méthode "reverse" permet d'inverser l'ordre de la liste
# Tout comme la méthode "sort", la méthode "reverse" écrase la liste à le contenu de la liste à laquelle on l'applique
# Par l'inverse de cette même liste
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
employes.reverse()
print(employes)