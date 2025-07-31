# El programa debe pedirle al usuario con input() que ingrese una cadena de texto (una palabra o frase), 
# para verifica si es un palíndromo. Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha y de derecha a izquierda, ignorando los espacios y las mayúsculas, ejemplo: "reconocer“ y "Anita lava la tina“.
# str.lower() para convertir la cadena a minúsculas.
# str.replace(" ", "") para eliminar los espacios dentro el str
# Recuerda las formas de hacer slicing de arreglos y revertir sus elementos o caracteres.
# NOTA: str.replace(" ", "") reemplaza todas las apariciones de un carácter o subcadena en toda la cadena y str.strip() elimina los espacios en blanco, pero solo al principio y al final de la cadena.

frase = input('Digite la farse a determinar si es Un palíndromo: ').strip().lower().replace(' ', '')
frase_reversa = frase[::-1]

if frase == frase_reversa:
    print(f' "{frase}" SII es un palíndromo')
else:
    print(f' "{frase}" NOO es un palíndromo')
    