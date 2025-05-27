# Ejercicio 2
"""
Construir una contraseña segura combinando especificas de los datos personales del uduario mediante indexado
y slicing.

Los datos son:

npmbre
apellido paterno
apellido materno
fecha de nacimiento(AAAA-MM-DD)

Construye con la siguiente lógica:

Letra inicial del nombre
ultimas 2 letras del apellido paterno
guion bajo
primera letra del apellido materno
día de nacimiento

para poder digitar los datos desde el teclado usamos:

input ("digita el nombre")
int (input ("Digita el nombre : "))
"""


nombre = input ("Digita el nombre : ")
apellido_paterno = input ("Digita tu apellido paterno : ")
apellido_materno = input ("Digita tu apellido materno : ")
fecha_nacimiento = input ("Digita tu fecha de nacimiento (AAAA-MM-DD) : ")
print(f'¡Hola {nombre} {apellido_paterno} {apellido_materno} {fecha_nacimiento}!')

print(f'tu password es : {nombre[0]}{apellido_paterno[-2:]}_{apellido_materno[0]}{fecha_nacimiento[-2:]}')