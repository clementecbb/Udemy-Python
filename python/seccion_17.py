 # Encapsulamiento
 
class A():
    def __init__(self):
        self.contador = 0
         
    def increment(self):
        self.contador += 1
        
    def cuenta(self):
        return self.contador
    
class B():
    def __init__(self):
        self.__contador = 0
         
    def increment(self):
        self.__contador += 1
        
    def cuenta(self):
        return self.__contador
    
a =A()

#print("objeto1")
#print(a.cuenta())
a.increment()
#print(a.cuenta())
#print(a.contador)


b =B()
#print("Objeto 2")
#print(b.cuenta())
b.increment()
#print(b.cuenta())
#print(b.__contador)


# Profundizar encapsulamiento

class X():
    def __init__(self):
        self._contador = 0
        self._cuenta = 0 # el guion bajo (_) indica que no se haga lo que abajo indica que es incorrecto porque es un atributo encapsulado
        
    def incrementar(self):
        self._contador += 1
    
    def cuenta(self):
        return self._contador
    
x =X()
#print(x.cuenta)  # esta forma es incorrecta    (que no haga ese tipo de impresion)
#x.cuenta = 20   # que no cambie el atributo de esa manera
#print(x.cuenta)   # que no vuelva a imprimir el atributo de esta manera



# Metodos Get Y Metodo Set (para cambiar valores o ver su valor)

class Y():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0
        
    @property # dice que esto va a ser tomado como un metodo get y puede ser llamado como si fuera un atributo
    def cuenta(self):
        return self._cuenta
    
    @cuenta.setter # Metodo set (modifica un atributo)
    def cuenta(self, cuenta):
        self._cuenta = cuenta
    
    @property # Metodo Get
    def contador(self):
        return self._contador    
    
    @contador.setter
    def contador(self, contador):
        self._contador = contador
    
y = Y()
#print(y.cuenta) # forma correcta de llamar a traves de un metodo
#print(y.contador)

y.cuenta = 20
y._contador = 50
#print(y.cuenta)
#print(y.contador)




# Herencia (tener 1 o mas clases que hereden a otras, clases padres y clases hijas)


class Animales():
    def habla(self):
        print("yo soy un animal")
    def descripcion(self):
        print("yo soy un {}".format(self.animal))
        
class Perro(Animales): # todos los atributos de la clase animales ahora estaran en la clase perro
    pass


class Abejas(Animales): 
    def __init__(self, animal):
        self.animal = animal

#animal = Animales()
#animal.habla()


#perro = Perro()
#perro.habla()

#abeja = Abejas("abeja")
#abeja.descripcion()



# Profundizar herencia

class Autos():
    def __init__(self, marcas):
        self.marcas = marcas
        
class AutoElectrico(Autos):
    def __init__ (self, marcas , sonido): # para heredar todo correcto hay que agregar super() y agregar el atributo dentro de init
        super().__init__(marcas)
        self.sonido = sonido

#autoelectrico = AutoElectrico("geometry", False)
#print(autoelectrico.marcas)
#print(autoelectrico.sonido)



# Herencia multiple



class Alpha():
    def primera(self):
        return "esta es la clase Alpha"
    
    
class Beta():
    def segunda(self):
        return "esta es la clase Beta"

class Gama(Alpha, Beta):
    pass


gama= Gama()
#print(gama.primera())
#print(gama.segunda())



# Polimorfismo (2 objetos distintos usan el mismo metodo)


class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    def hablar(self):
        print(self.mensaje)
        
    
class Perro(Animales):
    def hablar(self):
        print("yo hago guau")
        
class Pez(Animales):
    def hablar(self):
        print("yo no hablo")
        
perro = Perro("Guau")
#perro.hablar()

animal = Animales("miau")
#animal.hablar()

pez= Pez("glug glug")
#pez.hablar()



#ejercicio 1
print("Ejercicio 1" )

class Estudiantes():
    def __init__(self ,nombre ,nota):
        self.nombre = nombre
        self.nota = nota
        
    def imprimir(self):
        print("Nombre: {} \nNota: {}".format(self.nombre, self.nota))
    
    def resultados(self):
        if self.nota < 4:
            print("Reprobado")
        else:
            print("Aprobado")

estudiante1 = Estudiantes("Carlos", 3)
#estudiante1.imprimir()
#estudiante1.resultados()

estudiante2 = Estudiantes("Anastasia",6)
#estudiante2.imprimir()
#estudiante2.resultados()


#ejercicio 2
print("Ejercicio 2" )

class Calculadora():
    def __init__(self):
        self.valor1 = int(input("Ingrese el valor 1: "))
        self.valor2 = int(input("Ingrese el valor 2: "))
        
    def suma(self):
        self.suma = self.valor1 + self.valor2
        print (self.suma) # o se puede poner return self.suma

    def resta(self):
        self.resta = self.valor1 - self.valor2
        print (self.resta)

    def multi(self):
        self.multi = self.valor1 * self.valor2
        print (self.multi)
        
    def div(self):
        self.div = self.valor1 / self.valor2
        print (self.div)

calculadora = Calculadora()
#calculadora.suma()
#calculadora.resta()
#calculadora.multi()
#calculadora.div()

# Ejercicio 3
print("Ejercicio 3")

class Fabrica():
    def __init__(self,llanta,color,precio):
        self.llanta = llanta
        self.color = color
        self.precio = precio
        
class Moto(Fabrica):
    def datos(self):
        print("La moto: la cantidad de llantas: {}, el color: {}, el precio: ${}".format(self.llanta, self.color, self.precio))
    
class Carro(Fabrica):
    def datos(self):
        print("El carro: la cantidad de llantas: {}, el color: {}, el precio: ${}".format(self.llanta, self.color, self.precio))

moto = Moto(2,"rojo",2000)
#moto.datos()
carro= Carro(4,"negro",10000)
#carro.datos()


#Ejercicio 4
print("Ejercicio 4")


class Marino():
    def hablar(self):
        print("hola")
        
class Pulpo(Marino):
    def hablar(self):
        print("soy un pulpo")
        
class Foca(Marino):
    def hablar(self,mensaje):
        self.mensaje = mensaje
        print(self.mensaje)


pulpo = Pulpo()
#pulpo.hablar()

foca = Foca()
#foca.hablar("soy una foca")



#Ejercicio 5 
print("Ejercicio 5")


class Universidad():
    def __init__ (self,Nombre):
        self.Nombre =Nombre
    
class Carrera():
    def especialidad(self,especialidad):
        self.especialidad = especialidad
        
class Estudiante(Universidad,Carrera):
    def datos(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("mi nombre es: {},tengo {} años, mi especialidad es {}, estudio en la universidad {}".format(self.nombre, self.edad,self.especialidad,self.Nombre))
        
        
persona = Estudiante("U Andes")
persona.especialidad("ing")
persona.datos("clemente",21)