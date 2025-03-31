import turtle


fenetre = turtle.Screen()
fenetre.bgcolor("white")  


tortue = turtle.Turtle()
tortue.color("blue")      
tortue.pensize(3)        


for _ in range(4):
    tortue.forward(100)   
    tortue.right(90)      


fenetre.exitonclick()
