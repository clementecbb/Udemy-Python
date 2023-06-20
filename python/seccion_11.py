#diccionarios

diccionario = {"usuarios" : "clemente", "contraseña" : 12345}
#               clave          valor        clave      valor

diccionario2= {"nombre" : "clemente", "apellido" : "barros"}

#print(diccionario)#         llama al diccionario
#print(diccionario.keys())#      llama solo las claves del diccionario
#print(diccionario.values())#        llama solo los valores del diccionario
#print(diccionario["usuarios"])#        llama solo a la llave usuario dentro del diccionario

#diccionario["edad"] = 20#           agrega una nueva clave y valor al diccionario

#diccionario.pop("usuarios")#        elimina la clave usuario y su valor
#diccionario.clear()#                elimina el contenido del diccionario
#print(diccionario.get("contraseña"))#        entrega el valor de la clave contraseña (trae valores )
#diccionario.setdefault("edad",20)#          produce una nueva clave y su valor 
#diccionario.update(diccionario2)#                        junta un diccionario con otro ya existente
#diccionario.copy()#                             copia el diccionario
#print(diccionario)


#ejercicio 1

capitales= {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
seleccionado=input("ingrese un pais: ")


if(capitales.get(seleccionado)!=None):
    print("la capital de tu pais ingresado es:", capitales.get(seleccionado))
else:
    print("ese pais no se encuentra")



#ejercicio 2
jugadores = {1 : "Casillas", 15 : "Ramos", 3 : "Pique", 5 : "Puyol", 11 : "Capdevila", 14 : "Xabi Alonso", 16 : "Busquets", 8 : "Xavi Hernandez", 18 : "Pedrito", 6 : "Iniesta", 7 : "Villa"}
numero=int(input("Ingresa un numero: "))

if(numero in jugadores):
    print("el jugador que porta ese numero es", jugadores.get(numero))
else:
    print("no existe ese jugador")
