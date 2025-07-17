# # ***************La Precedencia Matemática
# La regla de precedencia matemática en Python establece el orden en que se evalúan 
# los operadores dentro de una expresión. Los operadores con mayor precedencia se ejecutan primero, 
# y en caso de operadores con igual precedencia se siguen reglas de asociatividad 
# (por ejemplo, potencias se asocian de derecha a izquierda, otros operadores de izquierda a derecha).

# #*****************Reglas de la precedencia de operadores en Python:
# 1️⃣. Los paréntesis () tienen la precedencia más alta y siempre sirven para forzar un orden específico 
# en la evaluación de expresiones.

# 2️⃣. La potenciación ** es asociativa a la derecha, es decir, en una expresión como 2 ** 3 ** 2 se evalúa 
# primero 3 ** 2 y luego el resultado eleva a 2:
# 2 ** (3 ** 2)  # equivalente a 2 ** 9 = 512

# 3️⃣. Los operadores de multiplicación *, división /, división entera // y módulo % tienen la misma precedencia 
# y se evalúan de izquierda a derecha.

# 4️⃣. La suma + y resta - tienen precedencia menor que la multiplicación y división, 
# pero mayor que los operadores de desplazamiento y lógicos, y también se evalúan de izquierda a derecha.

# 5️⃣. Las comparaciones (<, <=, >, >=, ==, !=), junto con los operadores de identidad 
# (is, is not) y pertenencia (in, not in), tienen una precedencia intermedia.

# 6️⃣. Los operadores lógicos not, and y or tienen la menor precedencia, y se evalúan en ese orden: 
# primero not, luego and, y finalmente or.


# print('precedencia.py')

print((2+2) * 10**2 /5)  # 80.0 paréntesis, potenciación, mult, sum y rest

print( 2 + 2  * 10**2 / 5) #42.0


print(2 ** 3 ** 2)   # calcula 2 ** (3 ** 2) = 2 ** 9 = 512
print((2 ** 3) ** 2) # calcula (2 ** 3) ** 2 = 8 ** 2 = 64

a, b = 6

x = a
x %= b      #* x = x % 2 = 1
print('x %= b:', x)