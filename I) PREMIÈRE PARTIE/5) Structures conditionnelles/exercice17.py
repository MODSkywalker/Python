# Remettre la structure conditionnelle dans l'ordre
# Dans cet exercice, tu dois remettre la structure conditionnelle <strong>dans l'ordre
# Voici le texte qui doit être affiché selon les conditions :
# Note plus petite que 3 : Sans commentaire...
# Note supérieure ou égale à 3 et inférieure à 6 : Tu n'as rien compris !
# Note supérieure ou égale à 7 et inférieure à 10 : Il faut tout revoir...
# Note supérieure ou égale à 11 et inférieure à 14 : Peut mieux faire.
# Note supérieure ou égale à 15 et inférieure à 18 : Bon travail !
# Note supérieure ou égale à 18 et inférieure à 20 : Excellent !!
# Note égale à 20 : C'est un sans faute !
# Attention : Tu ne dois pas modifier les conditions en tant que tel, juste l'ordre des if / elif.
# N'enlève pas le print à la fin de l'exercice et ne modifie pas les 3 premières lignes


# Ligne à ne pas modifier
import sys
note = sys.argv[-1]
commentaire = ""

# Change l'ordre des if / elif
# if note < 3 :
#     commentaire = "Sans commentaire..."
# elif note >= 3:
#     commentaire = "Tu n'as rien compris !"
# elif note > 6 :
#     commentaire = "Il faut tout revoir..."
# elif note > 10 :
#     commentaire = "Peut mieux faire."
# elif note > 14 :
#     commentaire = "Bon travail !"
# elif note >= 18 and note < 20:
#     commentaire = "Excellent !!"
# elif note == 20:
#     commentaire = "C'est un sans faute !"


# Solution 1
if note < 3:
    commentaire = "Sans commentaire..."
elif note == 20:
    commentaire = "C'est un sans faute !"
elif note >= 18 and note < 20:
    commentaire = "Excellent !!"
elif note > 14:
    commentaire = "Bon travail !"
elif note > 10:
    commentaire = "Peut mieux faire."
elif note > 6:
    commentaire = "Il faut tout revoir..."
elif note >= 3:
    commentaire = "Tu n'as rien compris !"
# Ne modifie pas la ligne ci-dessous
print(commentaire)