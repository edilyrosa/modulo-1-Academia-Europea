
import os
ARCHIVO = 'tareas.txt'

def agregar_tarea(tarea):
    if tarea.strip() == '':
        print(' ⚠️ Debe ingresar una tarea')
        return
    with open(ARCHIVO, 'a', encoding='utf-8') as f: # *el append de la tarea en el archivo 
        f.write(tarea + '\n')                       #*Ejecuto la operacion de agregarlo al final 
    print('✅Tarea agregada con exito')
    
def mostrar_tareas():
    if not os.path.exists(ARCHIVO):
        print(' ⚠️ El archivo que sea mostrar no existe')
        return
    with open(ARCHIVO, 'r', encoding='utf-8') as f: 
        tareas = f.readlines()                      
    if not tareas:
         print(' ⚠️ El archivo de tareas esta vacio')
    else:
        print(' 📃 -------------- Lista de Tareas ------------------ 📃')
        for i, t in enumerate(tareas, start=1):  # * la recorremos y formamos las instancias de index y tarea 
            print(f'{i}. {t.strip()}')              # * Imprimimos index y tarea
             
def modificar_tarea():
    if not os.path.exists(ARCHIVO):
        print(' ⚠️ El archivo que sea mostrar no existe')
        return
    with open(ARCHIVO, 'r', encoding='utf-8') as f: 
        tareas = f.readlines()                      
    if not tareas:
         print(' ⚠️ El archivo de tareas esta vacio')
    else:
        print(' 📃 -------------- Lista de Tareas ------------------ 📃')
        for i, t in enumerate(tareas, start=1):  # * la recorremos y formamos las instancias de index y tarea 
            print(f'{i}. {t.strip()}')  
    
    # *Programamos la modificacion de la tarea
    
    num = input('Diga el numero de la lista a modificar: ').strip()
    if not num.isdigit() or not (1 <= int(num) <= len(tareas)):
        print(' ⚠️ Numero de opcion invalido')
        return
    nueva = input('Escribe la nueva tarea: ').strip()
    if nueva == '':
        print(' ⚠️ la tarea no puede ser0 vacia')
        return
    tareas[int(num) - 1] = nueva + "\n"  
    with open(ARCHIVO, 'w', encoding='utf-8') as f: 
        f.writelines(tareas)
    print('✍🏽 Tarea modificada exitosamente')
    print('✍🏽 La lista de Tareas ha quedado asi: ')
    mostrar_tareas()
    
def borrar_archivo():
    if os.path.exists(ARCHIVO) and os.path.getsize(ARCHIVO) > 0: #*getsize(ARCHIVO) retorna el tamano del archivo en bytes
        os.remove(ARCHIVO)
    else:
        print('⚠️ No hay nada que borrar')

def main():
    while True:
        print('====== GESTION DE TAREAS ==========')    
        if not os.path.exists(ARCHIVO): #*Si no existe
            print('1. Agregar tarea')
            print('2. Salir del Sistema')
            opcion = input('Elige una opcion: ').strip()
            if opcion == '1':
                tarea = input('Escribe la tarea: ')
                agregar_tarea(tarea)
            elif opcion == '2':
                print(' 👋🏽 Saliendo... ')
                break
            else: 
                input(' ⚠️ Opcion Invalida ')
        else: #menu compelto
            print('1. Agregar tarea')
            print('2. Mostrar tareas ')   
            print('3. Modificar tareas ')   
            print('4. Borar el archivo de las tareas (tareas.txt) ')   
            print('5. Salir del Sistema')   
            opcion = input('Elige una opcion: ').strip()
            if opcion == '1':
                tarea = input('Escribe la tarea: ')
                agregar_tarea(tarea)
            elif opcion == '2':
                mostrar_tareas()
            elif opcion == '3':
                modificar_tarea()
            elif opcion == '4':
                borrar_archivo()
            elif opcion == '5':
                print(' 👋🏽 Saliendo... ')
                break
            else: 
                input(' ⚠️ Opcion Invalida ')
main()