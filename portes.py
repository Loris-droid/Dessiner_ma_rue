# Dépendances
from ma_rue import rue, affiche
from rectangle import rectangle
from couleur_aleatoire import couleur_aleatoire
from math import pi
from random import randint


# Définitions

# Fonction portes()
def portes(x,y):
    '''
    Dessine une porte de 50 pixels en largeur et 70 pixels en hauteur
    La forme du haut de la porte est aléatoire rectangulaire ou arrondi
    La couleur pleine de remplissage est choisi aléatoirement parmi les couleurs HTML valides
    Paramètres :
        x est l'abcisse du milieu de la base de la porte
        y est l'ordonnée du sol du niveau de la porte        
    '''     
     
    if randint(1, 2) == 1 :
        rectangle(x, y, 30, 50, couleur_aleatoire())
    else :
        rue.begin_path()
        rue.move_to(x+15, y)
        rue.line_to(x-15, y)
        rue.arc(x, y-35, 15, pi, 2*pi, False)
        rue.close_path()
        rue.fill_style = couleur_aleatoire()
        rue.fill()
        rue.stroke() 
        
        
# Tests
if __name__ == '__main__':
    affiche(rue)
    for i in range(21) :
        portes(0 + i * 40,rue.height)