# import datetime 
# datetime = datetime.datetime

from datetime import datetime 
#print(dir(datetime))

hoy = datetime.now()
print(hoy)
dia_semana = hoy.weekday()  # 0 = lunes, 6 = domingo
semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
print(semana[dia_semana])


#formarear nla fecha: 2025-08-20 22:46:20.170583
fecha_formateada1 = hoy.strftime('%d/%m/%Y %H:%M:%S')
fecha_formateada2 = hoy.strftime('%Y-%m-%d  %H:%M:%S')
fecha_formateada3 = hoy.strftime('%a %d %b %Y, %I:%M%p')

print('Fecha formateada:', fecha_formateada1, '|', fecha_formateada2, '|', fecha_formateada3) #20/08/2025 22:52:59 | 2025-08-20  22:52:59 | Wed 20 Aug 2025, 10:52PM
