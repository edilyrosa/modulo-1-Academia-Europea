mi_lista = [1,3,4,5,6,6,6]
mi_set = {1,3,4,5,6,6,6}
print(type(mi_lista))
print(type(mi_set))
print('la lista', mi_lista)
print('el set', mi_set)
print('el set tamano', len(mi_set))
print('esta? 6 en set? ', 6 in mi_set)
for ele in mi_set:
    print(ele)

mi_set.add(100)
print('el set', mi_set)
mi_set.update([101, 102, 103])
print('el set + lista ', mi_set)

#mi_set.remove(500) #!KeyError: 500
mi_set.discard(500) #sin error, unque no existe 
mi_set.remove(101)
print('el set son 101 ', mi_set)

mi_set.clear()
print('el set limpio ', mi_set) #el set limpio  set()

set_uno = {1,2}
set_dos = {3,4}
set_tres = set_uno.union(set_dos)
print(set_tres) #{1, 2, 3, 4}

set_ahora_list = list(set_tres)
set_ahora_tupla = tuple(set_tres)
print(set_ahora_list) #[1, 2, 3, 4]
print(set_ahora_tupla) #(1, 2, 3, 4)