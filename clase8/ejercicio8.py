# Escribe un programa que defina y recorra la siguiente matriz (o lista de listas) de 3x3. 
# matriz = [ [0, 1, 1],   fila 0
# 		     [1, 0, 1],  fila 1
# 		     [1, 1, 0] ] fila 2
# Debes recórrela e imprimir en pantalla únicamente los valores que se encuentran 
# en las posiciones de la diagonal principal de la matriz, los cuales son: 0 0 0 encuentra 
# el patrón para lograrlo.


matriz = [ ["e", 1, 1], #matriz[0][0] = 0
		   [1, "l", 1], 
		   [1, 1, 'i'] 
        ]

vertor_fr =  ['m',
              'p',
              'u',
              'u',
              ]
#(i == j) #*patron

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j: print(f'L diagonal Principal es [{i}][{j}] = {matriz[i][j]}') 


# print(len(vertor_fr))
# print(len(matriz))