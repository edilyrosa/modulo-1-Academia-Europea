
# *Las funciones se definen con def name(args): bloque
# ? 1. Sin Parametros/argumentos ni retorno de valores.

#fun_saludar() #!Error: NameError: name 'fun_saludar' is not defined
def fun_saludar():
    print('Hola como estas?')
    print('--'*30)
    
fun_saludar()
#casos...
fun_saludar()
fun_saludar()
fun_saludar()


x = 100
def imprime():
    print(f"la var global es {x}")
    print(f"la var global sumada es es {x+10}")
    print('**'*30)
    
print(f"Desde afuera la var global es {x}")
imprime()


def imprime_dos():
    x = 22.2
    print(f"la var local es {x}")
    print(f"la var local sumada es es {x+10}")
    print('#'*30)


imprime_dos()
print(f'test x + 10 = {x+10}')

# ? 2. Con Parametros/argumentos ni retorno de valores.

def fun_saludar_parametro(nombre):
    print(f'Hola, como estas? mi nombre es: {nombre}')
    print('--'*30)
    
fun_saludar_parametro('Carlos') #*✅
#fun_saludar_parametro() #!TypeError: fun_saludar_parametro() missing 1 required positional argument: 'nombre'
#fun_saludar_parametro('Carlos', 'hola') #!TypeError: fun_saludar_parametro() takes 1 positional argument but 2 were given

def fun_saludar_parametro_clave(saludo, nombre):
    print(f'{saludo} {nombre}')
    print('**'*30)
    
fun_saludar_parametro_clave('Carlos', 'Hola, como estas? mi nombre es:')                #*con orden
fun_saludar_parametro_clave(nombre='Carlos', saludo='Hola, como estas? mi nombre es:')  #*puede ser SIN orden



def fun_saludar_parametro_opcional(nombre, saludo = 'Hola, como estas? mi nombre es: '):
    print(f'{saludo} {nombre}')
    print('**'*30)
    
fun_saludar_parametro_opcional('Carlos', 'Holiiiiiiiiiiiiiiiiiiiii: soy ')               
fun_saludar_parametro_opcional(nombre='Edily')  
fun_saludar_parametro_opcional(nombre='Marta') 



# ? 3. Con Parametros/argumentos CON retorno de valores.
def sumar(a, b):
    '''
    esta funcion tiene parametros 
    que al ser llamada se sumaran
    mas instruciones
    '''
    resultado = a + b
    # print(resultado)
    return resultado

total = sumar(5,5) + 20
print(sumar(5,5))
print(total)

# sumar(10, 2)

def multi(a,b): return a*b 

print(multi(5,5))


def info_usuario():
    """
    este es un comentario 
    de explicacion
    para que mi conpanero lo termine.
    esta es una funcion para hacer fetch de info desde una API
    """
    nombre='Marta'
    edad=20
    return nombre, edad

info = info_usuario()
print(info)
print(info[1])

#* Desempaquetar ele de una tupla
nombre_u, edad_u = info_usuario()
print(nombre_u, edad_u)



#*  instrucción PASS
def fun_por_def(args):
    #codifica lo qie hablaos
    pass
    
# fun_por_def()

print(info_usuario.__doc__) #solo muestra o imprime el docstring

help(sumar) #muestra mas, su firma y parámetros

