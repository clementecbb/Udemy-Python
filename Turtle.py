import turtle
import random 

s = turtle.Screen()
s.title("primer proyeto")
s.bgcolor("black")


j1 = turtle.Turtle()
j1.hideturtle()
j2 = turtle.Turtle()
j2.hideturtle()
j1.shapesize(2,4,1)
j2.shapesize(2,4,1)

j1.color("yellow","red")

j2.color("yellow","blue")


j1.penup()
j1.goto(200,200)
j1.pendown()
j1.circle(40)

j1.penup()
j1.goto(-250,225)
j1.showturtle()


j2.penup()
j2.goto(200,-200)
j2.pendown()
j2.circle(40)

j2.penup()
j2.goto(-250,-170)
j2.showturtle()

dado= [1,2,3,4,5,6]

for i in range(20):
    if j1.pos()>= (200,200):
        print("Gano la nave Roja")
        break
    elif j2.pos()>= (200,-200):
        print("Gano la nave Azul")
        break
    else:
        turno1= input("presiona el Enter para avanzar.")
        turno1 = random.choice(dado)
        print("Salio",turno1, "avanzas:",turno1*20)
        j1.pendown()
        j1.forward(20*turno1)

        turno2= input("presiona el Enter para avanzar.")
        turno2 = random.choice(dado)
        print("Salio",turno2, "avanzas:",turno2*20)
        j2.pendown()
        j2.forward(20*turno2)



turtle.done()

