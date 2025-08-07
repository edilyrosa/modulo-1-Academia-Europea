edad = 30
print('hola', 'tengo', edad, sep='*', end=': ')
print('hola', 'tengo', edad, sep='*')

import time 
for i in range(5):
    print(i, end=' ', flush=True)
    time.sleep(1)