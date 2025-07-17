# # ***************Los operadores de Asignación en Python 
# Sirven para asignar valores a variables y actualizar esos valores. 
# El operador básico es =, que asigna directamente un valor, pero existen operadores compuestos 
# que combinan una operación con la asignación.

# *****************Operador básico de asignación
# = asigna el valor de la derecha a la variable de la izquierda.
# x = 7  # x recibe el valor 7


# ******************Operadores de asignación compuestos
# Permiten realizar una operación con el valor actual de la variable y luego 
# asignar el resultado a esa misma variable. Son equivalentes a escribir la operación completa 
# con asignación, pero en forma abreviada.


# ®️Resumen
# ✅El operador = asigna un valor directamente.
# ✅👀🤯Los operadores compuestos (+=, -=, *=, etc.) modifican la variable basándose en su valor actual.
# ✅Son útiles para escribir código más limpio y eficiente.


# print(10%4)  #2

x = 5

x += 5 #! x = x + 5

x -= 2

x *= 10

x /= 2

x //= 4

x %= 4

x **= 0

print("Resultado", (x)) # *Resultado 1.0


a = 7
b = 2
x = a 
x+=b # x = x + b 
print('x+=b', x)
x = a
x-=b
print('x-=b', x) #x-=b 5


# *********************🤯👀 Mirar Propiedades de las potencias
# 0 elevado a la 0 está indefinido matemáticamente. Pero en Python 𝟎^𝟎  = 1
# Esto es porque, y para evitar ambigüedades en cálculos y funciones, Python define 0**0 como 1
print('0**0 = ', 0**0) # *0**0 = 1
print('2**-3 = ', 2**-3) # *2**-3 = 0.125
print('(1/3)**-2 = ', (1/3)**-2) # *(1/3)**-2 =  9.000000000000002