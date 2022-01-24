# Structure conditionnelle if
age = 20
if age >= 18:
    print("Vous êtes majeur !")
elif age < 18:
    print("Vous êtes mineur !")

# L'emploi du else
user = "Paul"
if user == "admin":
    print("Accès autorisé !")
elif user == "root":
    print("Accès autorisé !")
else:
    print("Accès refusé !")
