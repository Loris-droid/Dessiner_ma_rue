def trait(x1,y1,x2,y2):
    '''
    dessine un trait entre les 2 points transmis en paramètres
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    
    '''
    rue.begin_path()
    rue.move_to(x1, y1)
    rue.line_to(x2, y2)
    rue.close_path()
    rue.stroke()