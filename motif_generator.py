import turtle
from PIL import Image
import time

def generer_motif(n_sides=4, taille=80, repetitions=10, angle=30, couleur="multi", option=["decroissant", "croissant","spiral"]):
    """
    Dessine un motif géométrique répété.
    
    Paramètres :
    - n_sides : nombre de côtés du polygone 
    - taille : longueur de chaque côté
    - repetitions : combien de fois on répète le motif en tournant
    - angle : angle entre chaque motif
    - couleur : couleur du tracé
    """
    

    arc_en_ciel = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
    filename = f"motif_{int(time.time())}.eps"
    filepath_eps = f"static/{filename}"
    filepath_png = filepath_eps.replace(".eps", ".png")
    
    
    
    turtle.clearscreen()
    fenetre = turtle.Screen()
    fenetre.bgcolor("white")  
    
    t = turtle.Turtle()
    t.pensize(2)
    t.speed(0)  # vitesse maximale

   
    for i in range(repetitions):
        for _ in range(n_sides): 
            
            
            if couleur == "multi":
                t.color(arc_en_ciel[i % 7]) # 7 est la taille de la liste arc en ciel
            else:
                t.color(couleur)  
                
                
            
            if "decroissant" in option:
                t.forward(taille*(1 - i / repetitions))
            elif "croissant" in option:
                t.forward(taille*(i / repetitions))  
            else:
                t.forward(taille) 
                
                
                
            
            t.right(360 / n_sides)
        t.right(angle)
        
        if "spiral" in option:
                t.penup()
                t.forward(4*i)
                t.pendown()                   

   
    canvas = turtle.getcanvas()
    canvas.postscript(file=filepath_eps)
    
    
    img = Image.open(filepath_eps)
    img.save(filepath_png, "png")
    
    return filepath_png.split("/")[-1]
    
