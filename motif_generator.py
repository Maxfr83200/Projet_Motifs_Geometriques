import turtle

def generer_motif(n_sides, taille, repetitions, angle, couleur):
    """
    Dessine un motif géométrique répété.
    
    Paramètres :
    - n_sides : nombre de côtés du polygone 
    - taille : longueur de chaque côté
    - repetitions : combien de fois on répète le motif en tournant
    - angle : angle entre chaque motif
    - couleur : couleur du tracé
    """
    
   
    fenetre = turtle.Screen()
    fenetre.bgcolor("white")  
    

    

    t = turtle.Turtle()
    t.color(couleur)
    t.pensize(2)
    t.speed(0)  # vitesse maximale

   
    for _ in range(repetitions):
        for _ in range(n_sides):          
            t.forward(taille)
            t.right(360 / n_sides)
        t.right(angle)                   

   
    fenetre.exitonclick()
    
    
if __name__ == "__main__":
    generer_motif(n_sides=3, taille=80, repetitions=12, angle=30, couleur="red")

