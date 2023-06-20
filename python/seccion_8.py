#ejercicio 1
x=input("ingrese una letra: ")
if x=="a":
    print("es vocal")
elif x=="e":
    print("es vocal")
elif x=="i":
    print("es vocal")
elif x=="o":
    print("es vocal")
elif x=="u":
    print("es vocal")
else:
    print("no es vocal")
    
    
    
#ejercicio 2

n = int(input("ingrese un numero para generar su valor absoluto: "))

if n < 0:
    print(n *-1)
else:
    print(n)
    

#ejercicio 3
#extraño--tamaño
#desligo--amigo
#riman--cuerpo
#sol--lol
x =input("ingrese la primera palabra: ")
y =input("ingrese la segunda palabra para ver si riman: ")
if x[-3: ]== y[-3: ]:
    print("Las palabras riman")
elif x[-2: ]== y[-2: ]:
    print("Las palabras riman un  poco")
else:
    print("Las palabras no riman")




#ejercicio 4

x= input("ingrese su candidato, A por el partido Rojo, B por el partido Verde y C por el partido Azul: ")
if x == "a":
    print("Usted ha votado por el partido Rojo")
elif x == "b":
    print("Usted ha votado por el partido Verde")
elif x=="c":
    print("Usted ha votado por el partido Azul")
else:
    print("opcion erronea")