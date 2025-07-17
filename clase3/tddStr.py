#*********************************************TIPOS DE DATOS: 
#2. ***********************************TDD str: 
#Son un o cadena de caracteres, entrecomillados por comillas dobles o simples (apostrofe).
# Con el operador “+” puedes “Concatenar” varios str para formar uno.
# “\” es el carácter de escape. \n, \t son sentencias de escape para str 

nombre = "Edily"
Apellido = 'Mora'
segundo_apellido = "Di'martino"

print(nombre+' '+Apellido+' '+segundo_apellido)

#print(' Edily Mora Di'martino ') #SyntaxError: unterminated string literal (detected at line 13)
print(''' Edily Mora Di'martino ''') 
print(''' Edily Mora Di'martino dijo: "que no" ''') 

#saltos de linea
print(
"""
Linea 1
Linea 2
Linea 3
"""
)

print("Linea 4\nLinea 5\nLinea 6")

print('Nombre \t Edad \t Peso \n Edily \t 33 \t 33.33')

#& ⛹🏽⛹🏽⛹🏽⛹🏽 EJERCICIO 2: Haz un print() saludando señalando tu nombre entrecomillas, di: "Mi nombre es: "Maria Perez" "
