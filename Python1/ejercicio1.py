"""
Ejercicio:

Simula el registro de un empleado nuevo, utilizando variables de diferentes tipos , mostrando
sis datos y validando su informacion con conversiones y tipos de datos


https://github.com/Racso2104/Automation-Master-.git
"""

#Paso 1 Registro de datos

nombre_empleado = "Oscar Esquivel"
edad = "37"
salario = "10.00"
inicial_del_departamento = "S"
esta_activo = True
no_departamento= "164"

print("Paso 1 ok")
# Paso 2 Mostrar tipo de datos original

print(type(nombre_empleado))
print(type(edad))
print(type(salario))
print(type(inicial_del_departamento))
print(type(esta_activo))
print(type(no_departamento))

print("Paso 2 terminado con exito")


# Paso 3 Convertir los datos

nombre_empleado = "20"
inicial_del_departamento = "2.0"

print(type (int (nombre_empleado)))
print(type (int (edad)))
print(type (float (salario)))
print(type (float (inicial_del_departamento)))
print(type (str (esta_activo)))
print(type (int (no_departamento)))


print("Paso 3 terminado con exito")

# Paso 4 Mostrar los nuevos tipos de datos despues de convertir
"""
print(type(nombre_empleado))
print(type(edad))
print(type(salario))
print(type(inicial_del_departamento))
print(type(esta_activo))
print(type(no_departamento))


print("Paso 4 terminado con exito")
"""
# Paso 5 Obtener el codigo ASCII del departamento
no_departamento= 164
print(chr(no_departamento))

# Paso 6 Imprimir la informacion


