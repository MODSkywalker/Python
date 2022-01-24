# On doit obtenir : https://www.docstring.fr/glossaire/

# Ne modifiez pas les variables ci-dessous
protocole = "https://"
nom_du_site = "docstring"
extension = "fr"
page = "glossaire"


# A l'aide de la concatenation
URL = protocole + "wwww." + nom_du_site + "." + extension + "/" + page + "/"
print(URL)

# A l'aide d'une f-string 
URL = f"{protocole}www.{nom_du_site}.{extension}/{page}/"
print(URL)


# A l'aide de la méthode format()
URL = "{}www.{}.{}/{}/".format(protocole, nom_du_site, extension, page)
print(URL)
URL = "{protocole}www.{domaine}.{extension}/{page}/".format(protocole=protocole, domaine=nom_du_site, extension=extension, page=page)
print(URL)