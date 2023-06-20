#funciones 

def saludo():
    print("hola")

#saludo()

def tabla():
    for i in range(10):
        print("7 X {} = {}".format(i,i*7))

#tabla()

#ejercicio 1

x = []

def numeros():
    i=0
    while i<= 5:
        y=int(input("ingrese algun numero: "))
        x.append(y)
        i=i+1
    print(x)

#numeros()
    



def ordenar():
    x.sort()
    par=[]
    impar=[]
    i=0
    for i in x:
        if i%2 ==0:
            par.append(i)
        else:
            impar.append(i)
        i=i+1
    print("lista de los pares {}, lista de los impares {}".format(par,impar))
    
#ordenar()


#ejercicio 2

def factorial():
    n=int(input("ingrese un numero: "))
    factorial=1
    for i in range(1,n+1):
        factorial= factorial*i
    print(factorial)

#factorial()

#Funciones Matematicas

#libreria de calculos matematicos
import math 

math.pow(10,2) # eleva un numero 
math.sqrt(64) # calcula la raiz cuadrada de un numero y da un resultado en float
math.isqrt(3) # calcula la raiz cuadrada y da un numero entero
math.sin(90) #calcula el valor de los senos
math.cos(90) # calcula el valor de los consenos 
math.tan(90) # calcula el valor de las tangentes
math.factorial(5) # calcula el factorial 

#libreria para entregar valores random
import random
random.randint(0,10) # entrega un numero aleatorio entre el rango que se le asigna

#retorno de funciones

def entero():
    print("este es un dato entero: ")
    return 10

#print(entero())

def decimal():
    print("este es un dato decimal: ")
    return 9,99

#print(decimal())

def frase():
    return "Hola Mundo"

#print(frase())

def asignacion():
    return 1,2,3,4,5

a ,b ,c , d, e = asignacion() #se asigna un numeros a cada letra
#print(a,e)


#ejercicio 3

def pedirnum():
    num1= int(input("ingrese un numero: "))
    num2= int(input("ingrese un segundo numero: "))
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0

#print(pedirnum())



#ejercicio 4

def iva():
    print("calcular iva de una cantidad")
    siniva=int(input("ingrese cantidad: "))
    
    respuesta=int(input("ingrese 1 si quiere agregar un % de iva especifico y un 0 si no: "))
    if respuesta ==1:
        porseniva=int(input("ingrese % de iva: "))
    else:
        porseniva= 21
    eliva= (siniva*porseniva)/100
    resultado=siniva+eliva
    return resultado

#print(iva())



#Parametros Y Argumentos

def suma(num1, num2):
    suma= num1+num2
    return suma

#print(suma(2,4))


#Variables globales

def valores():
    global num1 # vuelve una variable global
    global num2
    num1=110
    num2=40
    resultados= num1 + num2
    return resultados

#resta = num1 - num2
#print(resta)

#Valor Indefinido

def argumento(*num): # el * hace que se vuelva una tupla
    return type(num)

#print(argumento("hola"))


#ejercicio 5

def areacubo(base, altura):
    area=base*altura
    return area

def areacirculo(radio):
    area=(radio**2)*3.14
    return area
    
print(areacubo(3,4))
print(areacirculo(10))


#ejercicio 6

def muestra(*tupla):
    return len(tupla)

print(muestra(2,3,4,5,6,))