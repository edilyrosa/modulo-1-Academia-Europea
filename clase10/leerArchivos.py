
#*Leer (modo 'r'): leer TODO el contenido de un archivo que es te en la RAIZ
#?⭐Ese archivo a leer debe exister, crealo.
# with open('salida.txt', 'r') as f:
#   contenido = f.read()
#   print('El contenido de "salida.txt" es')
#   print(contenido)

# print('🏳️File leido')

#*con f.readline()
# #?⭐Ese archivo a leer debe exister, crealo.
# with open('salida.txt', 'r') as f:
#   #contenido = f.readline()
#   contenido = f.readlines()
#   print('El contenido de la 1era linea de "salida.txt" es')
#   print(contenido)
# print('🏳️File leido')

#*vamos a leer un file anidado, NO ESTA EN LA RAIZ
#?⭐Ese archivo a leer debe exister, crealo.
with open('../data/info.html', 'r') as f:
  contenido = f.read()
  print('El contenido de la 1era linea de "info.html" es')
  print(contenido)

print('🏳️File leido')

# <img src="https://">
# <img src="./assets/icon.pbg">