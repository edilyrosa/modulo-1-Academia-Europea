import os 
nombre_archivo = "nuevo.txt"
if not os.path.exists(nombre_archivo):
    with open(nombre_archivo, 'x') as f:
        #f.write('escribiendo en el nuevo file')
        pass
    print('Archivo creado')
else: print('El Archivo existe')