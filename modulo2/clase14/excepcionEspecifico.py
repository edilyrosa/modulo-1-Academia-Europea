
try:
    mi_lista = [1, 2, 3]
    print(mi_lista[4])  # Intento acceder a un índice que no existe
except IndexError as e:
    print('An exception occurred', e, type(e))  # Captura el error específico de índice
except IndexError as e:
    print('An exception occurred', e, type(e))  # Captura el error específico de índice
except IndexError as e:
    print('An exception occurred', e, type(e))  # Captura el error específico de índice
finally:
    print("FIN DEL PROGRAMA desde el finally, como cerrar archivos, conexiones, etc.")
    
print("FIN DEL PROGRAMA")
print("FIN DEL PROGRAMA")