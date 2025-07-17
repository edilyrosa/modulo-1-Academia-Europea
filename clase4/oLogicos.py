#edad_usurio = 20 
#? edad_usurio es mayor o igual a 18? True

# ***************Los operadores lógicos en Python (and, or, not) 
# se utilizan para "combinar expresiones booleanas" (que son True o False). 
# Permiten la tomar decisiones basadas en "varias condiciones al mismo tiempo".
print('Operadores Logicos: and, or, not')

# ***************Operador and (Y lógico):
# Devuelve True sólo si ambas condiciones son verdaderas.
# Si alguna es False, el resultado es False.

verdadero = True
falso = False
print(verdadero and False)      #False
print(verdadero and verdadero)  #True
print(not verdadero)            #False




temperatura = 20
hace_sol = True
if temperatura > 18 and hace_sol:
    print('deberiamos hacer un picnic 🌄') 
else:
    print('Mejor nos quedamos en 🏠') 
    

# ***************Operador or (O lógico):
# Devuelve True si al menos una condición es verdadera.
# Sólo devuelve False si todas las condiciones son falsas.

tengo_paraguas = False
if tengo_paraguas or hace_sol:
    print('deberiamos hacer un picnic 🌄') 
else:
    print('Mejor nos quedamos en 🏠') 



# ***************Operador not (Negación lógica):
# Invierte el valor booleano de una condición.
# Si la condición es True, not la convierte en False, y viceversa.
# #& ⛹🏽⛹🏽⛹🏽⛹🏽 EJERCICIO 1: como puedo expresar que: si es NO hace_sol deberia quedarme en casa