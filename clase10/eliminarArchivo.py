import os 
nombre_archivo_borrar = '../borrar.txt'

#* verificar que el archivo a eliminar existe
if os.path.exists(nombre_archivo_borrar):
    os.remove(nombre_archivo_borrar)
    print('Existe y fue borrado')  
else: print('El archivo NOO Existe')  