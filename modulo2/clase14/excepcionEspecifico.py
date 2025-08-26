
# try:
#     mi_lista = [1, 2, 3]
#     print(mi_lista[4])  # Intento acceder a un índice que no existe
# except IndexError as e:
#     print('An exception occurred', e, type(e))  # Captura el error específico de índice
# finally:
#     print("FIN DEL PROGRAMA desde el finally, como cerrar archivos, conexiones, etc.")
    
# print("FIN DEL PROGRAMA")
# print("FIN DEL PROGRAMA")

try:
    a = float(input('Ingresa un dividendo: '))
    b = int(input('Ingresa un divisor: '))
    resultado = a / b
    print('✅ el resultado es:', resultado)
except ValueError as e:
    print('❌ debe ingresar un nuemro 🔢', e, type(e))
except ZeroDivisionError as e:
    print('❌ no se puede dividir por cero 0️⃣', e, type(e))
except BaseException as e:
    print('❌ EL ERROR ES DE TIPO BASE ', e, type(e))
except Exception as e:
    print('❌ el error no lo se pero debe ser ', e, type(e))
# else:
#     print('✅ el resultado es:', resultado)
finally:
    print('🔚FIN DEL PROGRAMA')


print(" ⭐FIN DEL PROGRAMA DESDE FUERA⭐ ")