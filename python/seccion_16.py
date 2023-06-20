#Programacion Orientada a Objetos POO

#Clases Y Objetos

class FabricaTelefonos():
    pass

celular = FabricaTelefonos()
celular2 = FabricaTelefonos()

#Atributos Y Metodos

class TiendaTelefonos():
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128
    
    def llamar(self, mensaje): # metodo de instancia
        return mensaje
    
    def escucharmusica(self):
        print("Estas escuchando musica")
    
telefono = TiendaTelefonos()
telefono.marca
telefono.color
telefono.memoriaRam
telefono.almacenamiento
#print(telefono.almacenamiento)

#print(telefono.llamar("Hola"))
#telefono.escucharmusica()


# Self e Init

class FabricaAutos():
    marca = "BMW"
    
    def ElaborarVolvo(self):
        self.marca = "Volvo"
        
autos = FabricaAutos()
autos.ElaborarVolvo()
#print(autos.marca)

class FabricaPC():
    def __init__(self, marca, cpu):
        self.marca = marca
        self.cpu = cpu
        
pc = FabricaPC("Asus","Intel")
#print(pc.marca)
#print(pc.cpu)






# Metodos Especiales

#class Apple():
    #def __init__(self,modelo,color):
        #self.modelo = modelo
        #self.color = color
        #print("El objeto{} ha sido creado".format(self.modelo))
        
    #def __str__(self):
        #return "el objeto es {} ".format(self.modelo)
        
    #def __del__(self):
        #print("El objeto {} ha sido eliminado".format(self.modelo))
        
        
#iphone = Apple("iphone 11", "rojo")
#print(iphone.modelo)
#print(iphone)





# Profundizar POO

class FabricaRopa():
    def __init__(self, marca, *colores, **talla):
        self.marca = marca
        self.colores = colores
        self.talla = talla
    

ropa = FabricaRopa("DC", "negro", "rojo", "azul", s= 25, m=30, l= 35)
print(ropa.marca)
print(ropa.colores)
print(ropa.talla)
ropa.lana = 60
print(ropa.lana)