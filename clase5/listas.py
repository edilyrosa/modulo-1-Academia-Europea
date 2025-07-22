# & 1. LISTAS: son Colecciones ordenadas de datos, el orden es secuencial y preciso.
# Cada dato coleccionado es un elemento.
# La lista puede contener cualquier tipo de dato, incluso otras listas.
# Al elemento se accede por su posición (índice, que comienza desde 0), para:
# Obtenerlo, establecerlo, Modificarlo y Eliminarlo, entonces las listas son mutables.
#! Acceder a una posición fuera de rango, genera un error.
#* Se sabe su tamaño con la función len(), 🤯🤯🤯🤯👀👀👀🚩que cuenta desde 1
# Existen las Matrices (listas de listas), y accedes a los elementos del elemento lista con el 2do []


#? Se representa, encerrando sus elementos entrecorchetes []
lista_numeros = [1,2,3,4,'5', False]
print('mi lista ', lista_numeros)
#? Acceso a los elementos de una lista
print('Acceso al primer elemento de la lista: ', lista_numeros[5]) # False

#?Acceso con indices negativos
print('Acceso al penultimo elemento de la lista: ', lista_numeros[-2]) # "5"

#? Modificación de un elemento
lista_numeros[-2] = 5
print('Nuevo valor del  penultimo elemento de la lista: ', lista_numeros) # "5"

#?TDD de las Listas
print('TDD de una lista', type(lista_numeros)) # <class 'list'>
print('TDD del ultimo elemento', type(lista_numeros[-1])) # <class 'bool'>

#?Longitud de la lista

print(len(lista_numeros) == 0) #6

lista_nada = []
print('tamano de lista_nada', len(lista_nada)) #0


#?Matrices (listas de listas)
usurio_maria =['Maria', 'Paz', 20, True]
usurio_jose =['Jose', 'Marin', 40, False]
matriz_usuarios = [usurio_maria, usurio_jose]
print('Matriz', matriz_usuarios) # [['Maria', 'Paz', 20, True], ['Jose', 'Marin', 40, False]]
print('Primer elemento de la matriz', matriz_usuarios[0])
print('Primer elemento del elemento accedo de la matriz ', matriz_usuarios[1][2])

fru = ['manzana', 'pera', 'naranja']
print(fru) #!NameError: name 'fru' is not defined

matriz_usuarios[0][3] = 'Soltera'
print('Matriz modificada', matriz_usuarios) # [['Maria', 'Paz', 20, 'Soltera'], ['Jose', 'Marin', 40, False]]

nombre_usuario = 'Edily'
nombre_usuario = 123456
print