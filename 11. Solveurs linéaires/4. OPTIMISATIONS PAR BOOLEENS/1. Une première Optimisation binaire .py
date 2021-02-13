""" 
Une optimisation binaire utilise des variables de décision boléennes c'est soit 0, soit 1.


ETAPE1 : Décrire les contraintes booléenes dans un programme linéaire  :

    Les rêgles pour bien écrire les contraintes binaires ( Booléens) sont ici:
    https://www.youtube.com/watch?v=B3biWsBLeCw 

    Example : 
    Une entreprise a 5 projets parmis elle doit choisir un ou des projets parmis ces projets 

    Les variables de décisions sont donc : 

    xi =  { 1. Selectionné
            2. Non selectionné 

    Ensuite, pour exprimer différentes contraintes, on jour avec les contraintes binaires : ( Booléens)

    Si le projet 3 est sélectionné, alors le projet 5 ne peut pas être séolectionné  :
    On exprime ça comme ça 
    x3 + x5 <= 1 

    Seulement un des projets 2 et 3 doivent être sélectionné s'exprime comme ça : 
    x2 + x3 = 1

ETAPE 2 : CREER UN PROGRAMME LINEAIRE EN VARIABLES BOOLEENNES
    On a un bon example là : 
    https://www.youtube.com/watch?v=-3my1TkyFiM&t=56s


Sources et auteurs : 
    Integer Linear Programming | 0-1 Binary Constraints | Examples - Part 1
    https://www.youtube.com/watch?v=B3biWsBLeCw 
    https://www.youtube.com/watch?v=MO8uQnIch6I

"""

# Importer la librairie Pulp 
import pulp 
  