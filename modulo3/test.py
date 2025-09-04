# str = 'abcdef'
# def fun(s):
#    #! del s[2]
#     return s
# print(fun(str))


def fun(x):
    return 1 if x % 2 != 0 else 2
    # Si x es impar (x % 2 != 0), devuelve 1., Si x es par, devuelve 2.

print(fun(1)) # 1
#*la llamada se evalúa de adentro hacia afuera, como una cebolla.
print(fun(fun(1))) # 1 -> El resultado de la llamada interna (1) 
# se usa como el argumento para la llamada externa. La expresión se convierte en print(fun(1)).


print(len((1,))) #1

d = {1:0, 2:1, 0:1}
x = 0
for y in range(len(d)): #* # print(len(d)) -> se ejecuta 3 veces
   # x = 1 + x PUEDE MODIFICAR, SCOPE GLOBAL
   x = d[x] # * Valores a acada vuelta: 1, 0, 1
   
print(x) 

y = 16 
while y > 0:
    print("*", end='')
    y//=2
    

d = {'uno':1, 'tres':3, 'dos':2}
for k in sorted(d.values()):
    print(k, end=' ') # 1 2 3

# d.values(): Todos los valores del diccionario d, que son 1, 3 y 2.
# sorted() toma esos valores y los ordena en [1, 2, 3].