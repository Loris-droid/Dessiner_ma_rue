# Définitions
from ma_rue import rue, affiche 
# Fonction toit1()
def toit1(x, niveau):
    '''
    Dessine un triangle plein de couleur noir de 40 pixels de haut
    et avec une base de 160 pixels 
    Paramètres :
        x : abcisse du centre du toit
        niveau : numero du niveau (0 pour les rdc, ...)
    '''
    base = 160
    hauteur = 40


    base_triangle = rue.height - niveau * 60 # ordonnée de la base du toit
    sommet_triangle = base_triangle - hauteur
    
    rue.fill_style = 'black'
    rue.stroke_style = 'black'
    rue.begin_path()
    rue.move_to(x - base // 2, base_triangle)
    rue.line_to(x, sommet_triangle)
    rue.line_to(x + base // 2, base_triangle)
    rue.close_path()
    rue.fill()

# Test
if __name__ == '__main__':
    affiche(rue)
    toit1(rue.width/2, 0)
    for i in range(5) :
        for j in range(1, 6) :
            toit1(0 + 200 * i, j)