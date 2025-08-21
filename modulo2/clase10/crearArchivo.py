import os

nombre_archivo_crear = "archivo.txt"

if not os.path.exists(nombre_archivo_crear):
    with open(nombre_archivo_crear, "x") as f:
        pass  # Crear y cerrar el archivo sin escribir
    print("Archivo creado exitosamente.")
else:
    print("El archivo ya existe.")