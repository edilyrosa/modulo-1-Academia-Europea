
edad = int(input('Ingrese su edad: '))
ciudadano = input('Eres ciudadano? (si/no): ').strip().lower()
# if edad >= 18 and ciudadano == 'si':

if edad >= 18:
    if ciudadano == 'si':
        print('Eres mayor y eres ciudadano Puede votar')
    else:
        print('eres mayor, pero no eres ciudadano, no puede votar')
else:
    print('No eres mayor, no puede votar')