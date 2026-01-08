# Dépendances
from ma_rue import rue, affiche
from toit1 import toit1
from toit2 import toit2
from random import randint

# Définitions

# Fonction toits()

def toits(x, niveau):
    '''
    Dessine aléatoirement un toit plat ou un toit en pointe
    à l'ordonnée du niveau passé en paramètre
    Paramètres
        x : abscisse du centre de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    '''
    
    choix = randint(0,1)
    if choix == 0:
        toit1(x,niveau)
        
    else:
        toit2(x,niveau)

# Test
if __name__ == '__main__':
    affiche(rue)
    for i in range(5) :
        for j in range(6) :
            toits(0 + 200 * i, j)