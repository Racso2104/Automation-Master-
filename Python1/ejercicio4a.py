# Ejercicio 4

"""
Generacion de codigo
"""


nombre = input ("Digita el nombre completo : ")
apellido_materno = input ("Digita tu apellido materno : ")
clave_escolar = input ("Digita tu clave escolar de 8 caracteres alfanumericos : ")
print(f'¡Hola {nombre}  {apellido_materno} ')
clave_corta = clave_escolar[:-4]
nombre2 = nombre[::3]
print(clave_corta)
print(nombre2)
print(f'tu codigo es : {nombre[1]}{apellido_materno[len(apellido_materno)-1:]}{clave_corta[::-1]}{nombre2[0:2]}{clave_escolar[-2:]}')

print(f'tu C2 es : {nombre[1]}{apellido_materno[len(apellido_materno)-1:]}{clave_escolar[:-4][::-1]}{nombre[::3][0:2]}{clave_escolar[-2:]}')
