# Ejercicio 4 b

"""
Generacion de codigo
"""


nombre = input ("Digita el nombre completo: ")
apellido_paterno = input ("Digita tu apellido paterno : ")
apellido_materno = input ("Digita tu apellido materno : ")
CURP = input ("Digita tu CURP : ")
ingreso = input ("Digita tu año de ingreso a la empresa : ")
##print(f'¡Hola {nombre}  {apellido_materno} ')

##nombre2 = nombre[::3]

##print(nombre2)
##print(f'tu codigo es : {nombre[1]}{apellido_materno[len(apellido_materno)-1:]}{CURP[::-1]}{nombre2[0:2]}{CURP[-2:]}')

print(f'tu Codigo es : {nombre[2]}_{apellido_paterno[-1:]}_{apellido_materno[0:3][::-1]}_{CURP[-6:]}_ {nombre[0:8][::2]} _ {ingreso[-2:]}')