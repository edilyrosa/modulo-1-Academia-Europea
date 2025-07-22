
# 👀🤯Todos estos métodos:
# La lista los llama
# El índice comienza desde 0 
# Modifican la lista in situ, o sea el método altera directamente la lista original en memoria, 
# y queda cambiada. Menos los de consulta como index(ele)

# & 2. Medotos mas importantes de las listas

lista_test = [1, 2, 3, 4, 5]

# ?mi_lista.append(elemento): Añadir un elemento al final de la lista: 
print('original', lista_test)
lista_test.append(7)
#lista_test.append('hola')
print('con append', lista_test)



#? mi_lista.insert(indice, elemento): Añadir un elemento en una posición específica: 
# El nuevo ele se añade en la posición dada, desplaza una posicion hacia la derecha que que estaba alli.
# La posicion dada cuenta desde 0
lista_test.insert(5, 'seis')
print('con insert()', lista_test)


#? mi_lista.remove(elemento): Eliminar un elemento por su !!!⭐valor!!!!
# Elimina la primera ocurrencia del elemento especificado.
# Si el elemento no existe, genera un error ValueError.
lista_test.remove('seis')
print('con remove()', lista_test)


#* mi_lista.pop(posicion): eliminar un elemento por su !!!⭐indice!!!
# Elimina el elemento en la posición especificada y lo devuelve.
# Si no se especifica una posición, elimina y devuelve el último elemento de la lista.
# La posicion dada cuenta desde 0
lista_test.pop(5)
print('con pop()', lista_test)

#* mi_lista.clear(): eliminar todos los elementos de la lista, dejándola vacía.
# !lista_test.clear()
print('con clear()', lista_test)

#* mi_lista.index(elemento): Devuelve el índice del primer elemento encontrado con el valor especificado.
# Si el elemento no existe, genera un error ValueError.
lista_test.index(5)
print('con index()', lista_test.index(5))



#? mi_lista.sort(): Ordena los elementos de la lista.
#por defecto, ordena de menor a mayor (ascendente) 
# y con parametro reverse=True ordena de mayor a menor (descendente).
# Los elementos deben ser del mismo tipo para poder ordenarlos.
# Si la lista contiene elementos de diferentes tipos, genera un error TypeError.

lista_num = [5, 2, 9, 1, 5, 6]
print('original', lista_num)
lista_num.sort()
print('con sort()', lista_num)
lista_num.sort(reverse=True)
print('con sort() descendente', lista_num)

lista_letras = ['a', 'd', 'c', 'b', 'e']
print('original', lista_letras)





#!🚩👀 print('ordenadas', lista_letras.sort()) esto retorna None, no la lista ordenada, aca esta la pequena confucion de la clase!!🚩👀
lista_letras.sort()               #? Ordena la lista in situ
print('ordenadas', lista_letras)  #? ya la lista es ordenada

lista_palabras = ['banana', 'apple', 'cherry']
sorted(lista_palabras)
print('lista_palabras orifinal', lista_palabras)
print('Con sorted()', sorted(lista_palabras))  #? sorted() devuelve una nueva lista ordenada, no modifica la original

#? mi_lista.reverse(): Invierte el orden de los elementos de la lista.
lista_num_dos = [1, 2, 3, 4, 5]
print('original', lista_num_dos)    
lista_num_dos.reverse()
print('con reverse()', lista_num_dos)