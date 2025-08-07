# Desde un input, reciba de usuario todas las calificaciones 
# (separadas por whitespace) de los estudiantes de un curso. 
# Haga split() del str de calificaciones recibido y guárdalas 
# como elementos de una list, recórralos para procesarlos para 
# hacer print() de los siguientes datos:
# Nota promedio, formatea a 2 decimales con round(num, digitos).
# Mayor nota.
# Menor nota.

#* 'edily, carlos, ana'.split(', ')
calificaciones_str = input('Digite las calificaciones separadas por espacios ejn blanco: ')
calificaciones_lista = calificaciones_str.split()
print(calificaciones_lista) #['33', '45']

#?recorrerlos para sumarlos
acumulador_peromedio = 0
for calificacion in calificaciones_lista:
    acumulador_peromedio += int(calificacion)
    
    
promedio = round(acumulador_peromedio/len(calificaciones_lista), 2)
max_calificacion = max(calificaciones_lista, key=int)
min_calificacion = min(calificaciones_lista, key=int)

print('Calificaciones ingresadas', calificaciones_str) 
print(f'Calificion promedio {promedio}, la maxima calificacion es {max_calificacion} y la mas baja calificacion es {min_calificacion}') 