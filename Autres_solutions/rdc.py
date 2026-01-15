# Dépendances
from ma_rue import rue, affiche
from facade import facade
from portes import portes
from fenetre import fenetre

from random import randint

# Définitions

# Fonction rdc()
def rdc(x, couleur):
    '''
    Dessine le rdc sur une facade au niveau do sol de la rue
    avec une seule porte et 2 fenêtres placées aléatoirement.
    Paramètres
        x : abscisse du milieu de la base du RDC
        couleur : couleur fixée par l'immeuble        
    '''
    # Dessine la facade
    facade(x, couleur, 0)
    
    # Choix d'une distribution
    # (réinvestissement du CHIFOUMI, les str ont été vu mais pas les listes à ce stade )
    # proposer d'autres solutions de random sur les str en correction et évoquer les listes...
    k = randint(1,3)
    if k == 1 :
        distribution = 'pff'
    elif k == 2 :
        distribution = 'fpf'
    else :
        distribution = 'ffp'

    for i in range(-1,2) :
        if distribution[i] == 'p' :  # dessiner une porte
            portes(x+i*40, rue.height)
        else:  # dessiner une fenetre
            fenetre(x+i*40, rue.height)
    

# Tests
if __name__ == '__main__':
    from couleur_aleatoire import couleur_aleatoire
    affiche(rue)
    for i in range(7) :
        rdc( i * 160,couleur_aleatoire())

            