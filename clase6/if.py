#& 1. IF
#Se ejecuta un bloque si la condición es verdadera.
# Sintaxis: 
# if (condición lógica a evaluar) :
# 	indentación código py a ejecutar
#?Sentencia else
#Se usa para definir qué sucede si la condición del if es falsa. 
# Por eso NO LE SIGUE NINGUNA condición lógica a evaluar.  
# Se Ejecuta si ninguna condición previa es verdadera.
# #? Ejercicio: Determine si un número es par o impar

num = int(input('Ingrese un número: '))
if num % 2 == 0:
    print('el num es par')
else:
    print('el num es impar')