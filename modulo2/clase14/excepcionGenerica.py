

try:
    x = int(input("Ingrese un número: ")) 
    y = 10 / x
except Exception as e:
    # print("Ocurrió un error, por favor digite un numro:", e, type(e)) # !Ocurrió un error, por favor digite un numro: division by zero <class 'ZeroDivisionError'>
    print("Ocurrió un error, por favor digite un numro:", e, type(e)) # !Ocurrió un error, por favor digite un numro: division by zero <class 'ZeroDivisionError'>
else:                                                                   #!Ocurrió un error, por favor digite un numro: invalid literal for int() with base 10: 'y' <class 'ValueError'>
    print("El resultado es:", y)
finally:
    print("FIN DEL PROGRAMA desde el finally, como cerrar archivos, conexiones, etc.")
print("FIN DEL PROGRAMA")
print("FIN DEL PROGRAMA")
print("FIN DEL PROGRAMA")
print("FIN DEL PROGRAMA")
print("FIN DEL PROGRAMA")
