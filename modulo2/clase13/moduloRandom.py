

import random

#retorna un numro aleatorio de un dado con 6 caras
print('randrange(1, 7)', random.randrange(1, 7))
#imprime cara o cruz 0 o 1
print('randint(0, 1)',random.randint(0, 1))
#retorna un numro aleatorio de un dado con 6 caras
print('randint(1, 6)',random.randint(1,6))


#print('random()', random.random()*100)
print('random()', random.random())

# mezcla las cartas
cartas = ['A', 'B', 'C', 'D', 'E', 'F']
print('cartas originales', cartas)
random.shuffle(cartas) #none
print('cartas mezcladas', cartas)


#dime el ganador 
jugadores = ['Juan', 'Pedro', 'Maria', 'Ana']
ganador = random.choice(jugadores)
print('El ganador es:', ganador)


#seleciona los nuemros de la loteria.
numeros = random.sample(range(1, 50), 6)  # selecciona 6 numeros del 1 al 49
print('Los numeros de la loteria son:', numeros)