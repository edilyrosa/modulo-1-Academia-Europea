
#&********************************************  Slicing de listas
# Obtiener subsecuencias, cortando la lista. Sintaxis lista[inicio:fin:paso].
#*1. inicio: índice desde donde comienza el corte.
# Incluye el elemento en esta posición, Si se omite es 0, (índice 0).
# Puede ser negativo, contando desde el final (-1 es el último elemento).
#*2. fin: índice donde termina el corte. 
#👀🚩 NO incluye el elemento en esta posición, entonces + 1 -> (i+1)
# Si se omite va hasta el final.
# También puede ser negativo para contar desde el final (-1 es el último elemento).
#*3. paso: Indica de cuánto en cuánto se avanza para tomar elementos.
# Por defecto es 1, que significa que se toman elementos consecutivos.
# Puede ser un número negativo, lo que indica que la secuencia se recorre en sentido inverso (de atrás hacia adelante).
# ❌No puede ser 0 (causa un error).
lista_num = [1,2,3,4,5,6,7,8,9,10]
#? Elementos:{5-10}-> {i al i+1}

print('{5-10}', lista_num[4:10])            #{5-10} [5, 6, 7, 8, 9, 10]
print('{1-4}', lista_num[:4])               #{1-4} [1, 2, 3, 4]
print('{1-10 de 2 en 2}', lista_num[::2])   #{1-10 de 2 en 2} [1, 3, 5, 7, 9]

#? Paso negativo: recorrer al revés

print('{10-1}', lista_num[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print('{10-1} revr', lista_num[::-2]) # {10-1} [10, 8, 6, 4, 2]

#? 🧠✏️Consideraciones
# Si paso es positivo, inicio debe ser menor que fin para obtener elementos.
# Si paso es negativo, inicio debe ser mayor que fin, recorriendo al revés.
# El índice fin no está incluido en el resultado, sumale 1.

