# Crea una list con 5 elementos str de nombres de frutas en singular.
# Pide al usuario que ingrese el nombre de una fruta y, gurdala y normalizala con: input().strip().lower()
# Verifica si o no, la fruta digitada por usuario esta en tu lista e imprime un mensaje dependiendo de ello, el mensaje de mostrar el nombre de la fruta digitada por usuario y la list de frutas.


frutas = ['mango', 'fresa', 'melon', 'uva']
busqueda = input('Por favor digite el nombre de una fruta: ').strip().lower()

if busqueda in frutas:
    print(f'La fruta que escribio "{busqueda}" si esta en la lista {frutas}')
else:
    print(f'La fruta que escribio "{busqueda}" NOOO esta en la lista {frutas}')


#print(type(busqueda), busqueda)  

