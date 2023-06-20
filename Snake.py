import turtle
import time
import random


retraso=0.1
marcador=0
marcador_alto=0

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("black")
s.title("Snake")

sn=turtle.Turtle()
sn.speed(1)
sn.shape("square")
sn.penup()
sn.goto(0,0)
sn.direction = "stop"
sn.color("green")

c = turtle.Turtle()
c.shape("circle")
c.color("red")
c.penup()
c.goto(0,100)
c.speed(0)

cu = []

txt= turtle.Turtle()
txt.speed(0)
txt.color("white")
txt.penup()
txt.hideturtle()
txt.goto(0,-260)
txt.write("Marcador: 0 Marcador mas alto:0",align="center", font=("verdana",24,"normal"))


def arriba():
    sn.direction = "up"
    
def abajo():
    sn.direction = "down"
    
def derecha():
    sn.direction = "right"

def izquerda():
    sn.direction = "left"

def movimiento():
    if sn.direction =="up":
        y = sn.ycor()
        sn.sety(y+20)

    if sn.direction =="down":
        y = sn.ycor()
        sn.sety(y-20)
    
    if sn.direction =="right":
        x = sn.xcor()
        sn.setx(x+20)
    
    if sn.direction =="left":
        x = sn.xcor()
        sn.setx(x-20)
    
s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquerda, "Left")

    
while True:
    s.update()
    
    if sn.xcor() > 300:
        time.sleep(2)
        for i in cu:
            i.clear()
            i.hideturtle()
        sn.home()
        sn.direction = "stop"
        cu.clear()
    
        marcador =0
        txt.clear()
        txt.write("Marcador: {} Marcador mas alto:{}".format(marcador, marcador_alto),align="center", font=("verdana",24,"normal"))
        
        
    
    if sn.distance(c) <20 :
        x =random.randint(-250,250)
        y = random.randint(-250,250)
        c.goto(x,y)

        nc = turtle.Turtle()
        nc.shape("square")
        nc.color("green")
        nc.penup()
        nc.goto(0,0)
        nc.speed(0)
        cu.append(nc)
        
        marcador += 10
        if marcador > marcador_alto:
             marcador_alto = marcador
             txt.clear()
             txt.write("Marcador: {} Marcador mas alto:{}".format(marcador, marcador_alto),align="center", font=("verdana",24,"normal"))
        
    total=len(cu)
    for index in range(total -1,0,-1):
        x = cu[index-1].xcor()
        y = cu[index-1].ycor()
        cu[index].goto(x,y)
            
    if total > 0:
        x =sn.xcor()
        y =sn.ycor()
        cu[0].goto(x,y)
            
            
            
    movimiento()
    
    
    for i in cu:
        if i.distance(sn)<20:
            for i in cu:
                i.clear()
                i.hideturtle()
            sn.home()
            cu.clear()
            sn.direction ="stop"
                
    time.sleep(retraso)
    
    
turtle.done()