

# * Crea una función llamada division_segura(a, b) que:
def division_segura(a, b):
    try:
        return a / b #!⚠️Aaca es donde puede lanzarce la excepcion
    except ZeroDivisionError as e:
        return f"❌ El divisor no puede ser 0. Error de tipo: {type(e)}"
    except Exception as e:
        return f"❌ Ha ocurrido un error inesperado: {e}. De tipo: {type(e)}"
    finally:
        print("🔚 Fin del bloque try/except 1️⃣")

try:
    dividendo = float(input("Ingrese el dividendo: "))             #!⚠️Aaca es donde puede lanzarce la excepcion
    divisor = float(input("Ingrese el divisor, diferente a 0: "))  #!⚠️Aaca es donde puede lanzarce la excepcion
    # int('12.3')#!⚠️
except ValueError as e:
    print(f"❌ El número digitado no es numérico. Error de tipo: {type(e)}")
else:
    resultado = division_segura(dividendo, divisor)
    print("✅ El resultado es:", resultado)
finally:
        print("🔚 Fin del bloque try/except 2️⃣")




















# def division_segura(a, b):
#     try:
#         return a/b #!⚠️ aca es que puede ocurrir el error
#     except ZeroDivisionError as e:
#         return f'❌ No puedes dividir por 0. Tipo de Error: {type(e)}'
#     except BaseException as e:
#         return f'❌ Programa finalizo inesperadamente. Tipo de Error: {type(e)}'
#     except Exception as e:
#         return f'❌ Ha ocurrido un error de tipo: {type(e)}'
#     finally:
#         print('🔚 PRIMER bloque try/exception finalizado') 

# # print(division_segura(8, 1))
# try:
#     primero = float(input('Introduduca divi: ')) 
#     segundo = float(input('Introduduca divisor: '))
# except ValueError as e:
#     print(f'❌ El num difitado no es numerico. Error de tipo {type(e)}')
# except Exception as e:
#     print(f'❌ Ha ocurrido un error de tipo: {type(e)}')
# else:
#     resultado = division_segura(primero, segundo)
#     print(f'✅ El resultado es: {resultado}')
# finally:
#         print('🔚 SEGUNDO bloque try/exception finalizado')