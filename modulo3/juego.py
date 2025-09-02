"""
Juego de consola para 3 participantes con turnos aleatorios.

Se usan funciones del módulo math: fabs, ceil, floor, trunc, fmod, 
sqrt, isqrt, pow, pi, frexp, nan, isnan. Y del módulo random:  choice, uniform, randint, shuffle.

Incluye preguntas numéricas y de opción múltiple.
"""

import math
import random
RESTO_DESPRECIABLE = 1e-2 # = 0.01


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
        x = random.randint([10, 100])        
        return{
            'prompt': f'Usar math.isqrt({x}): = ?', 
            'tipo': 'int',                            
            'resp':math.isqrt(x)                       
        }
        
    if tipo == 'pow':
        a = random.randint([2, 6])        
        b = random.randint([2, 5])        
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
       # correcta = ele correcto
        prompt = f'Dado n={x}, math.frexp({x}) = m * 2 **e, cual es la opcion correcta ?\n'
        + '\n'.join([f'{i+1} {op} ' for i, op in enumerate(opciones)]), #enumerate retorna ele y su index
                              
        return{
            'prompt':  prompt, 
            'tipo': 'mc',
            #'resp': str(correcta+1)
            
        }