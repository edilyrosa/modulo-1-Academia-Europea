while True:
    try:
        x = int(input("Ingrese un número: "))
        resultado = 10 / x
        print(" ✅El resultado es:", resultado)
        break
    except (ZeroDivisionError, ValueError) as e:
        print(" ❌Ocurrió un error, por favor digite un numro:", e, type(e))
    except BaseException as e:
        print(" ❌Ocurrióde salida del sistema", e, type(e))
    except Exception as e:
        print(" ❌Ocurrió un error generico", e, type(e))
    finally:
        print(" 🔚FIN DEL PROGRAMA desde el finally, como cerrar archivos, conexiones, etc.")
        
print(" ⭐FIN DEL PROGRAMA DESDE FUERA⭐ ")   
