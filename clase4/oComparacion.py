# # ***************Los operadores de Comparación en Python 
# permiten "comparar dos" valores o expresiones y siempre devuelven un 
# resultado booleano (True o False). Usados para tomar decisiones en un programa, 
# por ejemplo dentro de estructuras condicionales (if, while, etc.).
# print('Operadores de Comparación: ==, !=, <, >, <=, >=')

# *************⁉️¿Cómo funcionan con tipo de dato numéricos?
# Es intuitivo, comparan sus valores numéricos naturalmente.
print(4 == 4.0) #True
print(4 >= 4.0) #T
print(5 >= 4) #T
print(4 != 4) #F

# *************⁉️¿Cómo funcionan con tipo de dato Booleanos?
# Se tratan como 1 (True) y 0 (False).
print(False < True) #True


# *************⁉️¿Cómo funcionan con tipo de dato String?
# ✅Se comparan lexicográficamente según el orden Unicode de cada carácter.
# Python compara cadena por cadena carácter a carácter, 
# 1. Python compara cadena por cadena 
print('''Hola' == "Hola" ''', 'Hola' == "Hola") # Hola' == "Hola"  True
print('''Hola' == "hola" ''', 'Hola' == "hola") # Hola' == "Hola"  False


# 2. Python compara carácter a carácter, 

print(ord('a'), ord('A')) #97 65
print("'a' > 'A'", 'a' > 'A') # 97 > 65 -> T, 'a' > 'A' True



# usando el valor numérico Unicode de cada carácter (obtenible con ord(caracter)).

# ✅La comparación se realiza en orden: se compara el primer carácter de ambas cadenas; 
# si son iguales, se pasa al siguiente, y así sucesivamente.
# El resultado es True o False según la relación entre las cadenas.
# 👀Las letras mayúsculas y minúsculas se diferencian porque tienen 
# valores Unicode distintos ('A' < 'a').

# ✅Solo puedes usar los operadores (==, !=, <, >, <=, >=) entre dos cadenas.



# 🚫No mezcles tipos diferentes, como str con int en comparaciones directas, porque no son compatibles, 
# si lo intentas usando operadores de orden (<, >, etc.), Python lanzará un TypeError. 
# Sin embargo, == y != sí pueden comparar distintos tipos siempre, retornando casi siempre False 
# (excepto casos especiales).
print("3" == 3)  # False  
# print("3" < 3)   #!  print("3" < 3)   # TypeError

# ®️🤯Resumen clave
# 👀Los operadores de comparación devuelven True o False.
# 👀Debes comparar preferentemente valores del mismo tipo para evitar errores.
# 👀Para cadenas, la comparación es lexicográfica, sensible a mayúsculas y minúsculas.
# 👀En tipos numéricos, se comportan naturalmente según valor.
# 👀== y != pueden comparar distintos tipos pero otros operadores NO.
print('"M" == 77', "M" == 77)           #*"M" == 77 False
print('ord("M") == 77', ord("M") == 77) #*ord("M") == 77 True
