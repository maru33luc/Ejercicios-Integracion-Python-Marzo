import re

print("Ejercicio 1")

num1=20
num2=25

def maxComunDivisor (num1,num2):
    mcd=2
    for i in range(1,25):
        if ((num1%i==0) and (num2%i==0)):
            mcd=i
    return mcd

mcd=maxComunDivisor(num1,num2)

print(mcd)        
            
print("Ejercicio 2")

def minComunMultiplo (num1,num2):
    for i in range(1,100):
        mcm=num1*i
        for i in range(1,100):
            x=num2*i
            if x==mcm:
                return x
                
mcm=minComunMultiplo(num1,num2)
print(mcm)        

print("Ejercicio 3")

texto = input("Introduce un texto: ")
diccionario_frecuencias = {}
def frecuenciaLetrasCadena (texto):
    quitar = ",;:.\n!\"'"

    for caracter in quitar:
        texto = texto.replace(caracter,"")
    texto = texto.lower()
    palabras = texto.split(" ")
    
    
    for palabra in palabras:
        if palabra in diccionario_frecuencias:
            diccionario_frecuencias[palabra]+=1
        else:
            diccionario_frecuencias[palabra]=1
    
    for palabra in diccionario_frecuencias:
        frecuencia = diccionario_frecuencias[palabra]            
        print(f"La palabra '{palabra}' tiene una frecuencia de '{frecuencia}'")
    

frecuenciaLetrasCadena(texto)

print("Ejercicio 4")


def devuelveTuplaPalabraMasRepetida(diccionario_frecuencias):
    mayorFrecuencia=0
    palabraMasFrecuente = " "
    for palabra in diccionario_frecuencias:
       
        if diccionario_frecuencias[palabra]>mayorFrecuencia:
            mayorFrecuencia=diccionario_frecuencias[palabra]
            palabraMasFrecuente= palabra
    tupla=(palabraMasFrecuente,mayorFrecuencia)            
    print(tupla)

devuelveTuplaPalabraMasRepetida(diccionario_frecuencias)
          
print("Ejercicio 5")

##Iterativa
def ingresaEntero():
    while True:
        try: 
            valor = int(input("Ingrese un numero: "))  
            break
        except:    
            print("El valor ingresado no es un entero")

ingresaEntero()        
        
print("Ejercicio 5 Recursivamente")
def ingresaEntero2():
    try: 
        valor = int(input("Ingrese un numero: "))  
    except:    
        print("El valor ingresado no es un entero")
        ingresaEntero2()

ingresaEntero2()

print("Ejercicio 6")

class DNIError (Exception):
    pass

class NombreInvalido(Exception):
    pass

class Persona():

    def __init__(self,nombre="",edad=0,dni=""):
        self.__nombre=nombre
        self.__edad=edad
        self.__dni=dni
        self.validar_dni()
        self.validarNombre()
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self,nombre):
        self.validarNombre()
        
    def validarNombre(self):
        while(True):
            try:
                if(re.search("^[a-zA-Z|ñÑ ]+$",self.__nombre)is not None):
                    print("validacion completa")
                    break
                else:
                    raise NombreInvalido
            except NombreInvalido as e:
                print("No es posible continuar(caracteres invalidos)")
                self.__nombre = str(input("Introduce el nombre completo: "))    

    def validar_dni(self):
        while(True):
            try:
                if len(self.__dni)!=9:
                    raise DNIError
                else:
                    break;
            except DNIError as e:
                print("DNI invalido.Ingrese el DNI nuevamente: ")
                self.__dni= input()
                
        while(True):
            try:
                num= int(self.__dni)
                break
            except ValueError as e:
                print("DNI Incorrecto, ingrese el DNI nuevamente (solo numeros): ")
                self.__dni= input(str())

    @dni.setter
    def dni(self,dni):
        self.__dni=dni
        self.validar_dni()
      
    @edad.setter
    def edad(self,edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad=0
        else:
            self.__edad=edad
    
    
    def mostrar(self):
        return "Nombre:"+self.__nombre+" - Edad:"+str(self.edad)+" - DNI:"+self.dni

    def esMayorDeEdad(self):
        return self.__edad>=18
    
p1 =Persona ("23a",23,"adad")


p1.edad = 30
print(p1.edad)
print(p1.dni)
print(p1.esMayorDeEdad())
print(p1.mostrar())

print("Ejercicio 7")   

class Cuenta():

    def __init__(self,titular,cantidad=0):
       self.__titular = Persona (titular.nombre,titular.edad,titular.dni)
       self.__cantidad = cantidad
       
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self,titular):
        self.__titular=titular

       
    def mostrar(self):
        return "Cuenta\n"+"Titular:"+ self.titular.nombre +" - Cantidad:"+str(self.cantidad)
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
    
    def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad
    
    
pers = Persona ("Maria",20,"234323456")
cuenta = Cuenta(pers,300)

print(cuenta.mostrar()) 
cuenta.retirar(10)
print(cuenta.cantidad)  

print("Ejercicio 8")

class CuentaJoven(Cuenta):

    def __init__(self,titular,cantidad,bonificacion=0):
        super().__init__(titular,cantidad)
        self.bonificacion=bonificacion
    
    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self.__bonificacion=bonificacion

    def mostrar(self):
        return "Cuenta Joven\n"+"Titular:"+self.titular.nombre+" - Cantidad:"+str(self.cantidad)+ "- Bonificación:"+str(self.bonificacion)+"%"
   
    def esTitularValido(self):
        return self.titular.edad < 25 and self.titular.esMayorDeEdad()
    
    def retirar(self,cantidad):
        if not self.esTitularValido():
            print ("No puesdes retirar el dinero. titular no válido")
        elif cantidad > 0:
            super().retirar(cantidad)
    

pers2 = Persona ("Juan",20,"234567678")
cuentaj = CuentaJoven(pers2,200,20)
print(cuentaj.esTitularValido()) 
print(cuentaj.mostrar())
