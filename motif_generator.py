import turtle
from PIL import Image
import os
import time

def figure(n_sides, taille, repetitions, angle, couleur, option, t):
    
    arc_en_ciel = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
    
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
        
        if "spirale" in option:
            t.penup()
            t.forward(4*i)
            t.pendown()
            
    
        
            

def dessiner_depuis_position(x, y, t):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    
    
    

def generer_motif(n_sides, taille, repetitions, angle, couleur, option):

    turtle.TurtleScreen._RUNNING = True 

    
    
    
    
    turtle.clearscreen()
    fenetre = turtle.Screen()
    fenetre.bgcolor("white")  
    
    t = turtle.Turtle()
    t.pensize(2)
    t.speed(0)  # vitesse maximale
    print(turtle.window_width(), turtle.window_height())
    
    
    if "coins" in option:
        positions = [(-480, 405), (480, 405), (-480, -405), (480, -405)]
        for pos in positions:
            dessiner_depuis_position(*pos, t)
            figure(n_sides, taille, repetitions, angle, couleur, option, t)
            if "miroir" in option:
                dessiner_depuis_position(*pos, t)
                t.right(180) 
                t.pendown() 
                figure(n_sides, taille, repetitions, angle, couleur, option, t)
            
        
    else:
        figure(n_sides, taille, repetitions, angle, couleur, option, t)
        if "miroir" in option:
                t.penup()
                t.home()
                t.right(180) 
                t.pendown() 
                figure(n_sides, taille, repetitions, angle, couleur, option, t)
    
    


                
    
                         

   
    

    eps_path = "static/images/motif.eps"
    png_path = "static/images/motif.png"
    
    
    canvas = fenetre.getcanvas()
    canvas.postscript(file=eps_path)

    turtle.bye()

    time.sleep(1)      # Attendre que l’EPS soit disponible (Windows a besoin d’une pause sinon bug)



    try:
        with Image.open(eps_path) as img:
            img.save(png_path)
    except Exception as e:
        print(f"Erreur lors de la conversion EPS -> PNG : {e}")
        return None

    
    os.remove(eps_path)  # Supprimer le fichier EPS temporaire

    return png_path
    
    