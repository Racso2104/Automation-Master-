"""
Ejercicio 2

Objetivo : Verificar manualmente (con print ) que las operaciones de indexado y slicing funcionan correctamente con
fiferentes strings

1.Imprime el primer carácter
2. Imprimer el último carácter
3. Imprime los primeros 4 caracteres
4. Imprime los ultimos 3 carácteres
5. Imprime el string invertido
6. Imprime el string in el primer y ultimo carácter
7. Imprime el String saltando de 3 en 3
8. Imprime la longitud total del string
"""

texto = "Murcielago"

#1.Imprime el primer carácter
print(f'El primer carácter es {texto[0]}')

#Imprimer el último carácter
print(f'El último carácter es {texto[-1]}')


# Imprime los primeros 4 caracteres

print(f'Lis primeros 4 carácteres son {texto[0:4]}')

# Imprime los últimos 3 caracteres

print(f'Los últimos 3 carácteres son {texto[-3:]}')

# 5. Imprime el string invertido

print(f'El String invertido {texto[::-1]}')

# 6. Imprime el string en el primer y ultimo carácter

print(f'El primer y último carácter es {texto[0]}{texto[-1]} ')

# 7. Imprime el String saltando de 3 en 3

print(f'Saltando de 3 en 3 {texto[::3]}')

# 8. Imprime la longitud total del string

print(f'La longitud de "{texto}" es : {len(texto)}')