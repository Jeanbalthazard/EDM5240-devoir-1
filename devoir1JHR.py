# #coding: utf-8

liste1 = list(range(30000,100000))
# J'ai créé une liste couvrant les numéros de permis pour les médecins admis entre 1930 et 1999.

liste1 = ["Gaëtan","Philippe","Yves"] # Substitution suggérée pour faire un test

for liste2 in range(0,18000):
    print(liste1, "{0:0>5}".format(liste2)) 

# J'ai créé un « loop » couvrant les numéros de permis pour les médecins admis entre 2000 et 2017. 
# Mais puisque de 0 à 9999, il manque d'un à quatre chiffres, j'ai ajouté la fonction format 
# (source : http://stackoverflow.com/questions/17118071/python-add-leading-zeroes-using-str-format), afin d'ajouter les chiffres manquants. 

### Pour distinguer mes commentaires des tiens, je les ai précédés de trois dièses.

### Ton script ne produit malheureusement pas le résultat attendu.
### La ligne 7, ci-dessus, affiche tout le contenu de la liste1 (70000 nombres) suivi du numéro de permis auquel on est rendu dans la liste2
### C'est ainsi que ton script affiche 1 260 000 000 nombres!
### Pour vérifier, change le contenu de la liste1 par [1,2,3] comme je te le propose dans la ligne 6, ci-dessus.

### En outre, ton script est identique, sauf pour un caractère à la ligne 7, à celui proposé par Félix Deschênes...
### J'en ai parlé avec Félix qui m'a expliqué.