# Variables
""""

Definicion:
En Python una variable se crea en el momento en que
se le asigna un valor

Sintaxis :(plantilla, forma , estructura)

snake_case

nombre_variable= valor

"""
from operator import truediv

x= 10
y= "Jose"


# Tipos de datos
"""
int (numeros enteros)
float / double (numeros decimales)
str (cadena de texto)
char (caracter)
bool (booleanos True or False)

"""

variable_entera=10
variable_entera=-10
variable_entera=0

variable_decimal= -100.02
variable_decimal= 50.0005
variable_decimal= 0.0

nombre = "Jose Sosa" # variable de tipo cadena
caracter = "a" # variable de tipo char

es_maestro = True
es_msero = False


# funcion Type -> permite saber el tipo de dato de una variable

print(type(variable_entera))
print(type(variable_decimal))
print(type(nombre))
print(type(caracter))
print(type(es_maestro))


print(type("@"))


# convertir de un tipo de dato a otro

number = 6

print(type (float (number)))

asccii = 65
print(chr(asccii))

# Conversiones validas

""""
str - int 
str - float
int - str
float - str 
float - int 
int - float
bool - int 
boll - str


"""


# Formato de impreesion en pantalla
print("Esto es un texto")
print("Esto es un texto", "otro texto", variable_entera)
print(nombre, "Esto es un texto", variable_decimal)
print('Hola mundo')


# F-string

print(f"formato f-string")
print(f"hola {nombre} ¿Como estas?")

"""
Ejercicio:

Simula el registro de un empleado nuevo, utilizando variables de diferentes tipos , mostrando 
sis datos y validando su informacion con conversiones y tipos de datos 

Paso 1 Registro de datos

Paso 2 Mostrar tipo de datos original 
Paso 3 Convertir los datos 
Paso 4 Mostrar los nuevos tipos de datos despues de convertir 
PAso 5 Obtener el codigo ASCII del departamento
Paso 6 Imprimir la informacion

"""
