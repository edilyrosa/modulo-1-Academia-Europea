#print(int('e')) #!ValueError: invalid literal for int() with base 10: 'e'
# Convertir lista de números a strings
#&Metodo map(function, iterables)
nums = [1, 2, 3]
nums_str = list(map(str, nums)) # ['1', '2', '3']
nums_cuadrados = list(map(str, nums)) #* ['1', '2', '3'] 👀 resultado de map()es un objeto map, por eso list() es un casteador.
print('Mapeamos cada ele para hacerlos str', nums_str) #Mapeamos cada ele para hacerlos str ['1', '2', '3']
