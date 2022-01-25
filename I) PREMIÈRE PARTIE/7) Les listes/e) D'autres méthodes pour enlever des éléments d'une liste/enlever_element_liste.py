# LES LISTES

# La méthode "pop" à l'inverse de la méthode "remove" permet d'enlever un élément de la liste 
# Par rapport à sa position et par rapport au nom de l'élément
# Cette stock l'élément enlever de sorte
# On peut donc la récupérer dans une variable
print("\t\tMéthode \"pop\"\n")
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
element_enleve = employes.pop(-1)
print(employes)
print("L'employé enlever est: " + element_enleve)

# La méthode "clear" est radicale
# En effet elle supprime tous les éléments de la liste
print("\n\t\tMéthode \"clear\"\n")
employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
employes.clear()
print(employes)