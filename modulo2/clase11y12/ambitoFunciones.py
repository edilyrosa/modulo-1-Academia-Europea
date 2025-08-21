x = 100

def mi_fun():
    x = 200
    y = 500
    print('desde mi fun', x, y)

print('desde fuera', x)
mi_fun()




print('__'*30)
a = 150
def mi_fun_scope():
    global a
    a +=50 #!UnboundLocalError: local variable 'a' referenced before assignment
    print('desde mi fun', a)

mi_fun_scope()
print('desde fuera', a)