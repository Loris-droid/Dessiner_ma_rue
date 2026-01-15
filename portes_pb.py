# Définitions
from ma_rue import rue, affiche
from rectangle import rectangle
from couleur_aleatoire import couleur_aleatoire
from math import pi
from random import randint
# Fonction portes()
def portes(x,y):
    '''
    Dessine une porte de 50 pixels en largeur et 70 pixels en hauteur
    La forme du haut de la porte est aléatoirement rectangulaire ou arrondi
    La couleur pleine de remplissage est choisi aléatoirement parmi les couleurs HTML valides
    Paramètres :
        x est l'abcisse du milieu de la base de la porte
        y est l'ordonnée du sol du niveau de la porte        
    '''    
    largeur = 30
    hauteur = 50
    couleur = couleur_aleatoire()

    forme = randint(0, 1)
    if forme == 0:
        rectangle(x, y, largeur, hauteur, couleur)
    else:
        rayon = largeur / 2
        centre_x = x
        centre_y = y - (hauteur - 15)
        rue.fill_style = couleur
        rue.stroke_style = 'black'
        rue.begin_path()
        rue.arc(centre_x, centre_y, rayon, pi, 0)
        rue.fill()
        rue.stroke()
        rectangle(x, y, largeur, hauteur - 15, couleur)

    
    # Tests
if __name__ == '__main__':
    affiche(rue)
    for i in range(21) :
        portes(0 + i * 40,rue.height)
