#TUPAS: muy parecidas a las listas, ordenas, index para acceder, sus ele inmulatbles
mi_lista = [1,2,3,4,5]
mi_tupla =  (1,2,3,4,5)
print( type(mi_lista), mi_lista, mi_lista[1], mi_lista[-1])
print( type(mi_tupla), mi_tupla, mi_tupla[1], mi_tupla[-1])

mi_lista[1] = True
#mi_tupla[1] = True #!TypeError: 'tuple' object does not support item assignment
print(mi_lista)
#*podemos recorrerla
print(mi_tupla[::-1]) #(5, 4, 3, 2, 1)
#*tamano 
print
print(len(mi_tupla)) #5

#*esta? ele IN iterable
print(5 in mi_tupla) #True

#*recorrerlo
for ele in mi_tupla:
    print(f'ele es {ele}') #ele es 1....

#*casting
nueva_lista = list(mi_tupla)
print(nueva_lista) #[1, 2, 3, 4, 5]
nueva_lista[1] = True 
print(nueva_lista) #[1, True, 3, 4, 5]


#*Desempaquetameinto de la tupla

uno, boo, tres, cuatro, cinco = mi_tupla
print(uno, boo) #1 2