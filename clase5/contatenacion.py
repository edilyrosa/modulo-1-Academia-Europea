hobbies = ['leer', 'correr', 'dibujar']
print('Mis hobbies son:', hobbies)  

hobbies_str = ', '.join(hobbies)

print( hobbies_str)
print('Mis hobbies son: ' + hobbies_str)

enun = 'Mis hobbies son: con += '
enun += hobbies_str

print(enun)
otro_hob = 2.22
print('Mis hobbies son: con FORMAT {} y {}'.format(hobbies[0], hobbies[1])) 
print('Mis hobbies son: con USANDO NUM  %s,  %s y %s  '%(hobbies[0], hobbies[1], (otro_hob))) 
print(f'Mis hobbies son: con FORMAT {hobbies[0]} y {otro_hob}') 