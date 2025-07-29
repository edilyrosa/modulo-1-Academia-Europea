# *************************************LISTAS
# sabemos obtener la posicion de un elemento: index(ele)
# sabemos acceder a elementos individuales por su Indexación (Indexing): letras[0], letras[-1] (último elemento)
# sabemos la longitud de la lista: len(mi_lista)

# sabemos insertar elementos: insert(i, ele), append(ele)
# sabemos eliminar elementos: remove(ele), pop(i), pop()
# sabemos limpiar o Vaciar la lista: clear()

# sabemos ordenar la lista: sort(), sort(reverse=True), sort(key=len), sort(key=abs), sort(key=abs, reverse=True), sort(key=str.casefold) 
# sorted(mi_list) -> Devuelve nueva lista, la original no cambia


#&Merging (fusionar) de listas: el orden importa
#? 1. Con el operador + (es como si lo concatenaras)

lista_uno = [1,2,3,4,5]
lista_dos = [6,7,8,9,10]
lista_final = lista_uno + lista_dos
print(lista_final) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_uno)    #[1, 2, 3, 4, 5]


#? 2. Con el operador de asignacion combinado += (es como si lo concatenaras)


lista_uno += lista_dos
print('con operador =+', lista_uno)   # con operador =+ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#? ⭐⭐EXTRA: Simple Asignacion es solo copia ni combina, es un espejo

lista_espejo = ['a', 'b', 'c']
lista_reflejo = lista_espejo
lista_reflejo.append('z')
print(lista_espejo) #['a', 'b', 'c', 'z']


#? 3. metodo mi_list.extend(iterable): combina dos iterables.

lista_uno.extend(lista_dos)
print('lista_uno con extend()', lista_uno) # lista_uno [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6, 7, 8, 9, 10]
lista_dos.extend('rosa')
print('lista_dos con extend()', lista_dos) # lista_dos con extend() [6, 7, 8, 9, 10, 'r', 'o', 's', 'a']



#? 4.  La sintaxis de unpacking con * para combinar listas ( [ *lista1, *lista2 ])
otra_lista = [5,6,7]
lista_desempaketada = [1,2,4, *otra_lista]

print('lista_desempaketada', lista_desempaketada) #[1, 2, 4, 5, 6, 7]

lista_empaketada = [1,2,4, otra_lista]
print('lista_empaketada', lista_empaketada) #lista_empaketada [1, 2, 4, [5, 6, 7]]


#?⭐⭐ EXTRA – Desestructuración para asignar variables desde una lista:
# lista_num = [100, 200, 33]
ele1, ele2, ele3 = [100, 200, 33]
print(ele2) #200