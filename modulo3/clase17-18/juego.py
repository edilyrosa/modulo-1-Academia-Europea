"""
Juego de consola para 3 participantes con turnos aleatorios.

Se usan funciones del módulo math: fabs, ceil, floor, trunc, fmod, 
sqrt, isqrt, pow, pi, frexp, nan, isnan. Y del módulo random:  choice, uniform, randint, shuffle.

Incluye preguntas numéricas y de opción múltiple.
"""

import math
import random
RESTO_DESPRECIABLE = 1e-2 # = 0.01
DEFAULT_ROUNDS = 8
#& EPSILON_FLOAT = 1e-2 # = 0.01

# * ----------------------------------Generamos las preguntas -----------------------------------------

    #*Debe retornar un dict prompt (pregunta), tipo (TDD de la operacion), resp (correcta)
def generar_pregunta():
    tipo = random.choice(['fabs', 'ceil', 'floor', 'trunc', 'fmod', 'sqrt', 'isqrt', 'pow', 'frexp', 'pi_area', 'nan'])
    
    # *Realizar Condicional por operación, para: Generar argumento(s) aleatorio(s), para ejecutar la operación. 
    if tipo == 'fabs':
        x = round(random.uniform(-25, 25), 1)         # *Argumento de la operacion 
        return{
            'prompt': f'Usar math.fabs(): |{x}| = ?', # *Mensaje que le imprimire a usuario para que resuelva la operacion.
            'tipo': 'num',                            # * Retorna float
            'resp':math.fabs(x)                       # *La respuesta correcta computada
        }
    
    if tipo in ('ceil',  'floor', 'trunc'):
        x = round(random.uniform(-25, 25), 2)
        if tipo == 'ceil':
            ans = math.ceil(x)
        elif tipo == 'floor':
            ans = math.floor(x)
        else: 
            ans = math.trunc(x)
            
        return{
            'prompt': f'Usar math.{tipo}({x}) = ?', 
            'tipo': 'int',                            
            'resp':ans                 
        }

    if tipo == 'fmod':
        a = round(random.uniform(5, 50), 2)        
        b = round(random.uniform(2, 9), 2)        
        return{
            'prompt': f'Usar math.fmod({a}, {b}): = ?', 
            'tipo': 'num',                            
            'resp':math.fmod(a, b)                       
        }
    
    if tipo == 'sqrt':
        x = random.choice([4, 9, 16, 25, 36, 49, 64, 81, 100])        
        return{
            'prompt': f'Usar math.sqrt({x}): = ?', 
            'tipo': 'num',                            
            'resp':math.sqrt(x)                       
        }
    
    if tipo == 'isqrt':
        x = random.randint(10, 100)    #TODO: Estaba random.randint([10, 100]), y espera 2 argumentos.
        return{
            'prompt': f'Usar math.isqrt({x}): = ?', 
            'tipo': 'int',                            
            'resp':math.isqrt(x)                       
        }
        
    if tipo == 'pow':
        a = random.randint(2, 6)  #TODO: Estaba random.randint([10, 100]), y espera 2 argumentos.  
        b = random.randint(2, 5)   #TODO: Estaba random.randint([10, 100]), y espera 2 argumentos.    
        return{
            'prompt': f'Usar math.pow({a}, {b}): = ?', 
            'tipo': 'num',                            
            'resp':math.pow(a, b)                       
        }
        
    if tipo == 'frexp':
        x = random.choice([4, 9, 16, 25, 36, 49, 64, 100])
        m, e = math.frexp(x)              
        opciones = [
            f'Exponente e = {e}',
            f'Exponente e = {e-1}',
            f'Exponente e = {e+1}',
            f'Exponente e = {-e}',
        ] 
        
        random.shuffle(opciones) # Cambio aleatorio del orden de los ele, de la lista de Op Mult
        correcta =  opciones.index(f'Exponente e = {e}') #aca atrapo el pos de la respiesta correcta
    
        #TODO: AGREGAR UN () a prompt o hacer sola linea pegada, indicando que prompt es toda una sola instruccion.
        prompt = (f'Dado n={x}, math.frexp({x}) = m * 2 **e, cual es la opcion correcta ?\n'
        + '\n'.join([f'{i+1}) {op} ' for i, op in enumerate(opciones)])) #*por iteracion f"{i+1}) {op}"
          #? enumerate(iterable) →  retorna ele e index del argumento iterable.
          #? metodo join([])      → De list a str: (“símbolo_separador”).join(my_list) 👀🚩Retorna 1 solo str con todos los elementos de la list
                                  
        return{
            'prompt':prompt, 
            'tipo': 'mc',
            'resp': str(correcta+1)
        }                        
    
    if tipo == 'nan':              
        opciones = [
            'float("nan") == float("nan") es True', #!False
            'math.isnan(float("nan")) es True', #*True
            'float("nan") < 1 es True', #!False
            '1 < float("nan") True', #!False
        ] 
        
        random.shuffle(opciones) # Cambio aleatorio del orden de los ele, de la lista de Op Mult
        correcta =  opciones.index('math.isnan(float("nan")) es True') #aca atrapo el pos de la respiesta correcta
    
        #TODO: AGREGAR UN () a prompt o hacer sola linea pegada, indicando que prompt es toda una sola instruccion.
        prompt = ('Cual de las siguientes expresiones sobre NaN es VERDADERA ?\n'
        + '\n'.join([f'{i+1}) {op} ' for i, op in enumerate(opciones)])) #*por iteracion f"{i+1}) {op}"
          #? enumerate(iterable) →  retorna ele e index del argumento iterable.
          #? metodo join([])      → De list a str: (“símbolo_separador”).join(my_list) 👀🚩Retorna 1 solo str con todos los elementos de la list
                                  
        return{
            'prompt':prompt, 
            'tipo': 'mc',
            'resp': str(correcta+1)
        }                        
    
    if tipo == 'pi_area':
        r = random.randint(2, 12) #radio aleatorio
        area = round(math.pi * (r ** 2), 2) 
        return{
            'prompt':f'Diga el area de un circulo con radio = {r}, usa math.pi con 2 decimales para tu respuesta = ?', 
            'tipo': 'num',
            'resp': area
        }
    
    return{
        
            'prompt':'Pregunta no definida', 
            'tipo': 'num',
            'resp': 0
        }


# *******************Validacion de la respuesta*******************

def revisar(pregunta, entrada):
    tipo = pregunta['tipo']
    correcta = pregunta['resp']
    
    if tipo == 'int':
        try:
            return int(entrada) == int(correcta)
        except:
            return False
    
    if tipo == 'num':
        try:
            val = float(entrada.replace(',', '.')) 
            return abs(val - float(correcta)) <= RESTO_DESPRECIABLE
        except:
            return False
    
    if tipo == 'mc':
        return entrada.strip() == str(correcta)
    else:
        return False
    
    

#*********************juego*********************

def jugar(jugadores,rondas=DEFAULT_ROUNDS):
    puntaje = { j:0 for j in jugadores}
    
    print('QUIZ MATEMATICO SIMPLE!!')
    print(f'Jugadores: {', '.join(jugadores)} | Rondas: {rondas}\n')
    
    for r in range(1, rondas+1):
        print('='*40) 
        print(f'Ronda {r}/{rondas}') 
        jugador = random.choice(jugadores)
        print(f'Es el turno de {jugador}')
        pregunta = generar_pregunta()
        print(pregunta['prompt'])
        entrada = input('Tu respuesta: ') 
        
        if revisar(pregunta, entrada):
            print('✅ Correcto !!')
            puntaje[jugador] +=1
            
    print('\n*****************RESULTADOS****************')
    # 1. mostraremos todos los jugadores y sus puntaje
    for j,p in puntaje.items():
        print(f'{j}:{p} punto(s)') 
        
    # 2. mostraremos el ganador o ganadores en caso de empate