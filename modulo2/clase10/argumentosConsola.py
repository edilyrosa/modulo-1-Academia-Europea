import sys
# sys.argv[0] -> nombre el archivo 
# sys.argv[1] -> 1er argumento pasado por usuario por consola
# sys.argv[2] -> 2do argumento pasado por usuario por consola

print('Nombre del script o archivo que usuario ejecuto', sys.argv[0]) 
print('TDD del 1er argumento', type(sys.argv[1]))  #class <str>

if len(sys.argv) > 1: #*si es TRUE es porque usuario envio aregumento, no solo ejecuto el script 
    print('El pimer argumento fue', sys.argv[1])
    print(f'El producto es "{sys.argv[1]}" y su precio es {sys.argv[2]} $')
    
else:
    print('Usuario NO paso argumentos')