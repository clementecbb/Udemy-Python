#Errores y Excepciones

while True:
    try:
        edad =int(input("ingrese su edad: "))
        print("Tu edad es: ",edad)
        break
    
    except:
        print("ingresaste un valor erroneo")
    
    finally:
        print("la ejecucion a finalizado")


#Excepciones Multiples

while True:
    try:
        num1= int(input("ingrese un numero: "))
        resultado=100/num1
        print(resultado)
    except ZeroDivisionError:
        print("no se pueede dividir entre 0")