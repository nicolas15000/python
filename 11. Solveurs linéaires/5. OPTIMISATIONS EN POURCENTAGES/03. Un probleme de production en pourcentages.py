""" 
cf : Recherche opérationnelle pour ingénieurs I (de Werra, Liebling, Hˆeche) ; page 33
documentation 5 en français sur nicolas15000 github

Un fabricant doit produire 120 kg d’un alliage comportant 30 % de plomb, 30 % de zinc et 40 % d’´etain.
Sur le marché, on trouve les alliages suivants :

alliage     1       2   3   4   5   6   7   8   9
% plomb     10      10  40  60  30  30  30  50  20
% zinc      10      30  50  30  30  40  20  40  30
% étain     80      60  10  10  40  30  50  10  50
coût/kg     4.1     4.3 5.8 6.0 7.6 7.5 7.3 6.9 7.3

Comment obtenir un alliage de la composition voulue dont le cout est minimum ? 

Formuler ce problème sous forme de programme linéaire. 

"""

# Solution :
# Notons 
# pi le pourcentage de plomb dans l’alliage i.
# zi le pourcentage de zinc dans l’alliage i.
# ei le pourcentage d’étain dans l’alliage i.
# ci le coût unitaire de production de l’alliage i.
# Introduisons les variables suivantes : xi = le nombre de kg de l’alliage i utilisés.
# 


# Notre fonction objectif est de réduire le cout unitaire
# Comme on a affaire à une matrice, on va pas réecrire chaque variable de décision et chaque valeur de cout 
# On réduit cela comme ça :
# Et le comme le nb de variables de décision est forcément de neuf donc de x1 ... à x9
# min (ci * xi)

# sous les contraintes  (30% = 0.30 de plomb, et 120 , c'est les 120 kgs nécessaires) ,
# Cette contrainte comprends donc une valeur de type "pourcentage" et une valeur de type "unitaire" mixée ensemble 
# tout simplement, 30% de 120kgs, peut aussi s'écrire 0.30 * 120 afin d'éliminer la fraction (niveau CM2 - école primaire)
# et donc 0.30 * 120 veut dire qu'on veut absolument que 30% du total de notre mélange soit du plomb: 
# Σ (pi * xi) = 0.30 * 120 

