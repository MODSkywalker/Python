# Dans cet exercice, vous devez :

# Afficher la phrase mdp_trop_court en majuscule si le mot de passe entré est égal à 0.
# Afficher la phrase mdp_trop_court avec une majuscule sur la première lettre si le mot de passe entré est plus petit que 8.
# Afficher la phrase "Votre mot de passe ne contient que des nombres." si le mot de passe entré ne contient que des nombres.
# Afficher la phrase "Inscription terminée." si le mot de passe est valide.

# Script de départ :

mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."
if len(mdp) == 0:
    print(mdp_trop_court.upper())
elif len(mdp) < 8:
    print(mdp_trop_court.capitalize())
elif mdp.isdigit():
    print("Votre mot de passe ne contient que des nombres.")
else:
    print("Inscription terminée.")