# El programa debe pedirle al usuario con input() que ingrese una cadena de texto (una palabra o frase), 
# con un bucle for recorra cada carácter y con  condicionales verificar si el carácter es una vocal (a, e, i, o, u).
# Finalmente, imprime:
# El número total de vocales que tiene la cadena.
# El número total de caracteres de la cadena.

frase = input('Ingrese la frase o palabra a analizar: ').strip().lower()
contador = 0
for chart in frase:
    if chart == 'a' or chart == 'e' or chart == 'i' or chart == 'o' or chart == 'u':
        contador +=1
print(f'El número total de vocales que tiene la cadena es {contador} y la cadena es de {len(frase)}')