# Crear un programa que busque un elemento específico en una lista, pedido por input(), define tu mismo 
# la lista y sus elementos. Recórrela con un bucle y Cuando lo encuentre, el programa
# debe imprimir su posición (índice) y detener la búsqueda inmediatamente con break. 
# Si el número no se encuentra después de revisar toda la lista, el programa debe informarlo.

# lista que recorrer creala tu
# un elemento que buscar ese se lo preguntas a usuario con input

el_num = int(input('Digite el elemento a buscar '))
lista_nums = [1, 55, 66, 101, 44, 0]
esta = False
for ele in lista_nums:
    if (el_num == ele): 
        print(f'El {el_num} y esta en la posicion {lista_nums.index(ele)}')
        esta = True
        break
if esta == False:
      print(f'El {el_num} NO esta en la lista: {lista_nums}')       
        
# for i in range(6)