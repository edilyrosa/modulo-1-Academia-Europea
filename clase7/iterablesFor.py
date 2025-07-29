
#& *****************************************Iterable
# Cualquier objeto que puedes recorrer elemento a elemento, es decir, un objeto sobre el que puedes iterar en un bucle 
# Las listas, tuplas, cadenas de texto, diccionarios, conjuntos son objetos iterable porque puedes recorrerlos con ciclo.
# Cuando usas un ciclo sobre un iterable, internamente se crea un iterador para ir obteniendo elemento por elemento.
#? 1. FOR:Recorre o itera sobre una secuencia 
#sintaxis: 
# for varEleIterado in iterable:
     # bloque de código usando varEleIterado

lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print('Ele - ', elemento) #Ele -  1...
    
for ele in lista:
    print('Eleva', ele**2)    #Eleva 4...

lista_new = []
for e in lista:
    lista_new.append(e**2)
print('lista_new', lista_new) #lista_new [1, 4, 9, 16, 25]

#? 2. 👀⭐⁉️🤯 puede establecer un condicional dentro de un bucle? CLARO

#lista = [1, 2, 3, 4, 5]
for ele in lista:
    if(ele %2 == 0):
        print(f'los pares son {ele}') # los pares son 2.. 4


#& 3. Sentencias de control dentro de bucles
#? break: Interrumpe y sale completamente del bucle, sin importar la condición del ciclo.
#lista = [1, 2, 3, 4, 5]
for i in lista:
    if(i == 3):
        break
    print(f'Imprimimos hasta 2, ele = {i}') 

#? continue: Salta el resto del código y pasa a la siguiente iteración.
for i in lista:
    if(i == 3):
        continue
    print(f'Imprimimos, ele = {i}') 

#? pass> No hace nada, es un marcador de posición (útil para mantener la sintaxis cuando quieres dejar código pendiente).
for i in lista:
    pass







#? 4. Bucles anidados (loops dentro de loops): para recorrer matrices y acceder a cada elemento.
# Una matriz es una lista de listas
# Cada ele de la lista principal es una FILA de la matriz (una lista). = 'i'
# Cada ele dentro de una fila es un valor en una COLUMNA. = 'j'
# matriz = [
#     [0, 1, 1],  # fila 0
#     [1, 0, 1],  # fila 1
#     [1, 1, 0]   # fila 2
# ]

# El bucle externo itera sobre las filas (i es el índice de fila).
# El bucle interno itera sobre las columnas (j es el índice de columna), elemento por elemento.

# Ejemplo para imprimir cada elemento con su posición:


matriz = [
    [1, 2, 3],  # fila 0
    [4, 5, 6],  # fila 1
    [7, 8, 9]   # fila 2
]

print('cuantos ele tiene matriz ',len(matriz)) # 3
# #?range(start, stop, step)
print('Elementos range esempaquetada', *range(6)) # 0 1 2 3 4 5
print(*range(1, 6)) #1 2 3 4 5
print(*range(3)) #0 1 2

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        valor = matriz[i][j]
        print(f'ele en fila {i} colum {j} es {valor}')
