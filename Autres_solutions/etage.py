# Dépendances
from ma_rue import rue, affiche
from facade import facade
from fenetre import fenetre
from balcon import balcon 

from random import randint

# Définitions

# Fonction etage()
def etage(x, couleur, niveau):
    '''
    Dessine sur une facade un étage avec 3 éléments choisis aléatoirement
    parmi une fenêtre ou une porte fenêtre avec balcon.  
    
    Paramètres
        x : abscisse du milieu de la base de l'étage
        couleur : couleur fixée par l'immeuble
        niveau : numéro de l'étage en partant de 0 pour le rdc
    '''
    y = rue.height - niveau * 60 # ordonnée de la base de l'etage
    
    # Murs
    rue.line_width = 1
    facade(x, couleur, niveau)
    # Eléments
    for i in range(-1,2):
        k = randint(0,1)
        if k == 0 : # dessiner une fenetre
            fenetre(x+i*40, y)
        else : # dessiner une porte fenetre avec balcon
            balcon(x+i*40, y)
            rue.line_width = 1    
            
# Tests
if __name__ == '__main__':
    from couleur_aleatoire import couleur_aleatoire
    affiche(rue)
    couleur = couleur_aleatoire()
    for n in range(6) :
        etage(rue.width/2,couleur,n)