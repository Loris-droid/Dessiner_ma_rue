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
    y = rue.height - 15 
    # Dessine la facade
    facade(x,couleur,0)
    
    # Choix d'une distribution
    pos1 = x
    pos2 = x - 40 
    pos3 = x + 40 
    position = randint(0,2)
    if position == 0:
        portes(pos1,400)
        fenetre(pos2,y)
        fenetre(pos3,y)
    if position == 1:
        portes(pos2,400)
        fenetre(pos3,y)
        fenetre(pos1,y)
    if position == 2:
        portes(pos3,400)
        fenetre(pos1,y)
        fenetre(pos2,y)

#Test
if __name__ == '__main__':
    from couleur_aleatoire import couleur_aleatoire
    affiche(rue)
    for i in range(7) :
        rdc(i*160, couleur_aleatoire())