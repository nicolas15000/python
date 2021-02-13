""" 
Une optimisation binaire c'est soit 0, soit 1.

Les rêgles pour bien écrire les contraintes binaires ( Booléens) sont ici:
https://www.youtube.com/watch?v=B3biWsBLeCw 

Example : 
Une entreprise a 5 projets parmis elle doit choisir un ou des projets parmis ces projets 

Les variables de décisions sont donc : 

xi =  { 1. Selectionné
        2. Non selectionné 

Ensuite, pour exprimer différentes contraintes, on jour avec les contraintes binaires : ( Booléens)



Sources and authors : 
Integer Linear Programming | 0-1 Binary Constraints | Examples - Part 1
https://www.youtube.com/watch?v=B3biWsBLeCw 
"""

# Importer la librairie Pulp 
import pulp 
  