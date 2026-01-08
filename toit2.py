
# Dépendances
from ma_rue import rue, affiche
from trait import trait
# Définitions

# Fonction toit2()

def toit2(x, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        
        niveau : num du niveau (0 pour les rdc, ...)
    '''
    y = rue.height - niveau * 60 # ordonnée de la base du toit
    
    
    # trait horizontal
    rue.line_width = 10
    rue.line_cap = "round"
    trait(x-80,y,x+80,y)
    

    rue.line_width = 1
    rue.line_cap = "butt"

# Test
if __name__ == '__main__':
    affiche(rue)
    for n in range(6) :
        toit2(rue.width/2, n)