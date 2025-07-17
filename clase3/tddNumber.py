

#3. ***********************************TDD int y float 
# int = enteros
# float = decimales

#***************************Generalidades de los numbers
# Pueden ser:
# Positivos o negativos 
# Expresados en potencia con el carácter "e"
# Son operando, valor o dato sobre el cual actúa un operador (aritmético y relacional) para realizar una operación.
# Operando: valor o variable que se usa como entrada para un operador. Ej: 44, 44.44, 4.8e3, ...
# Operador: símbolo o palabra que realiza una operación sobre uno o más operandos. Ej: +, _, *, /, >=, ...
 
#& ****************HAGAMOS OPERACIONES ARITMÉTICAS CON NÚMEROS 🧮📱
# ? OPERACIONES ARITMÉTICAS: se realizan entre int y float
# Suma: + 
# Resta: - 
# Multiplicación: * 
# División: / (resultado float) 
# División entera: // (resultado int) 
# Módulo (residuo): % 
# Potencia: **

print('Suma de int + int ', 3+3) #Suma de int + int  6
print('Resta de float - float ', 3.4-3.5) # Resta de float - float  -0.10000000000000009
print('Multipicacion de float * int ', 3.4*3) # SMultipicacion de float * int  10.2
#print('Restar de str - int ', "3.4"-3) #!TypeError: unsupported operand type(s) for -: 'str' and 'int'

#?CONVERSIONES
str()
int()
float("3.4")
print('Restar de float - int ', float("3.4")-3) # ✅Restar de float - int  0.3999999999999999

supuesto_false = bool(0) #False
supuesto_true = bool(1) #True
bool("") #False
bool("a") #True

print('supuesto_false', supuesto_false)
print('supuesto_true', supuesto_true)

print('bool + int', False + 3) #bool + int 3
print('bool + int', True + 3) #bool + int 4




#****************************?OTROS OPERADORES ARITMÉTICOS

#* División: / (resultado float) -> muestra parte decimal.
print('10/3 = ',10/3) #10/3 =  3.3333333333333335

#* División entera: // (resultado int) 👀  desprecia la parte decimal
print('10//3 = ',10//3) #10//3 =  3

#* Módulo (residuo): % 👀   devuelve el residuo (parte faccionaria)
print('10%3 = ',10%3) # 10%3 =  1
print('10%5 = ',10%5) #10%5 =  0

#* Potencia: ** 👀  Eleva la base
print('10**3 = ',10**3) # 10**3 =  1000



#?*************************Notación Científica “E”
# Para expresar una cifra numérica de forma más resumida mediante su exponente en base 10, con el carácter “e” 
#“e” Representa la potencia de 10 en notación científica, ®️ 2.5e3 = “2.5 multiplicado por 10 a la 3” =  2.5 × 10^3
# Puede ser E || e y el valor se guardará como TDD float, a menos que sea muy extensa.

#peso_total = -2.5e3 = 2.5 * 10^3 = -2.5 *1000 = -2.500
peso_total = -2.5e3 
print('peso_total es ', peso_total)#peso_total es  -2500.0
#peso_total_negativo = -2.5e-3 =  -2.5e-3 -0.0025
peso_total_negativo = -2.5e-3
print('peso_total_negativo es ', peso_total_negativo )#peso_total_negativo es  -0.0025

import keyword
print(keyword.kwlist)

edily = 'edily'
print(edily)

edily = 22.7
print(edily)


#!no reasignes las CONSTANTES !!
PI = 3.14
PI = 12