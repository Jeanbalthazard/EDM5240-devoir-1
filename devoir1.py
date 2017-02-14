# #coding: utf-8

liste1 = list(range(30000,100000))
# J'ai créé une liste couvrant les numéros de permis pour les médecins admis entre 1930 et 1999.

for liste2 in range(0,18000):
    print(liste1, "{0:0>5}".format(liste2)) 

# J'ai créé un « loop » couvrant les numéros de permis pour les médecins admis entre 2000 et 2017. 
# Mais puisque de 0 à 9999, il manque d'un à quatre chiffres, j'ai ajouté la fonction format 
# (source : http://stackoverflow.com/questions/17118071/python-add-leading-zeroes-using-str-format), afin d'ajouter les chiffres manquants. 
