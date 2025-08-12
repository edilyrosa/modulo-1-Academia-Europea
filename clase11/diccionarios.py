personaje = {
    'nombre':'mujer maravilla',
    'edad':33,
    'mujer':True,
     2:'dos'
}

print(type(personaje)) #<class 'dict'>
print(personaje['nombre']) #mujer maravilla
print(personaje[2]) #dos

print(personaje.keys()) #dict_keys(['nombre', 'edad', 'mujer', 2])
print(personaje.values()) #dict_values(['mujer maravilla', 33, True, 'dos'])
print(list(personaje.items())) # [('nombre', 'mujer maravilla'), ('edad', 33), ('mujer', True), (2, 'dos')]

for key in personaje:
    print(f'{key} -  {personaje[key]}')

for key, value in personaje.items():
    print(f'{key} -  { value}')
    
print(len(personaje)) #4


personaje['poderes'] = ['correr', 'volar']
personaje['edad'] = 50

print(personaje)

personaje.popitem()
print(personaje)

personaje.pop('edad')
print(personaje)


personaje.clear()
print(personaje) #{}

original = {"a":1, "b":2, "c":3, 'mi_lista':[1,2]}
copia = original.copy() # o con el constructor dirt()

copia["a"] = 11
copia["mi_lista"].append(3)
print(original)
print(copia)


import copy
original_deep = {"a":1, "b":2, "c":3, 'mi_lista':[1,2]}
copia_deep = copy.deepcopy(original_deep)

copia_deep['mi_lista'].append(33)
print(original_deep)
print(copia_deep)