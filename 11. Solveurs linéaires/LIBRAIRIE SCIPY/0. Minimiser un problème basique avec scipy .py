""" 
Minimiser                   w = 10*y1 + 15*y2 + 25*y3

Sous les contraintes:       y1 + y2 + y3 >= 1000
                            y1 - 2*y2    >= 0
                            y3 >= 340

avec                        y1 >= 0, y2 >= 0

Source fiable : https://stackoverflow.com/questions/49408242/scipy-optimize-linprog-difficulty-understanding-the-parameters
"""



import numpy as np
from scipy.optimize import linprog

# On prends le programme linéaire et on le transforme en matrice , 
# et vu que linprog a besoin de contraintes du type f(x) <= const, on doit tout inverser en  -f(x) <= - const : 
A = np.array([[-1, -1, -1], [-1,2, 0], [0, 0, -1], [-1, 0, 0], [0, -1, 0]])
b = np.array([-1000, 0, -340, 0, 0])

# Ici , on reconnait bien la fonction objectif à minimiser : 
c = np.array([10,15,25])

# On récupère le résultat de l'exécution du simplexe :
res = linprog(c, A_ub=A, b_ub=b,bounds=(0, None))

print('Optimal value:', res.fun, '\nX:', res.x)

# On voit que le résultat et y1 = 660 y2 = 0 et y3 = 340 pour une valeur globale de 15100
# ('Optimal value:', 15100.0, '\nX:', array([ 660.,    0.,  340.]))
# python3
# Optimal value: 15099.999961403426 
# X: [6.59999996e+02 1.00009440e-07 3.40000000e+02]