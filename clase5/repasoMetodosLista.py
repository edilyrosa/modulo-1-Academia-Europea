lista_numeros = [5, 2, 3, 1, 4, 6]
print('original', lista_numeros)
print(lista_numeros.append(7)) #none
print('con append()', lista_numeros)

# ordenar listas

lista_numeros.sort()
print('lista ordenada', lista_numeros)
lista_numeros.sort(reverse=True)
print('lista ordenada', lista_numeros)

# ordenando string
print("A" > "a") #False
lista_letras = ['c', 'A', 'a', 'b','B', 'C']
lista_letras.sort()
print('lista letras ordenada', lista_letras)

# criterios para ordenar unsando el atrb key
lista_nombres = ['Pedro', 'Juanes', 'Mariasssss', 'Ana']
lista_nombres.sort(key=len)
print(len(lista_nombres))
print(lista_nombres)

num = -10
print ('ahora es ', num) #-10
print ('ahora es ', abs(num)) #10

lista_num_abs = [1, -2, 10, 101, 3, -4, 5] 
lista_num_abs.sort(key=abs) #[1, -2, 3, -4, 5, 10, 101]
lista_num_abs.sort(key=abs, reverse=True) # [101, 10, 5, -4, 3, -2, 1]
print(lista_num_abs) 

lista_nom = ['Pedro', 'alba', "ana"]
lista_nom.sort() # ['Pedro', 'alba', 'ana']
lista_nom.sort(key=str.lower) # ['alba', 'ana', 'Pedro']
print(lista_nom )


lista_nom[-1] 
lista_nom.index(lista_nom[-1]) # 

print(lista_nom.index(lista_nom[-1]) )

print(lista_nom.index('Pedro') )