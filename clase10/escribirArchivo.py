#
#
# *Escribir con modo "w"
# 👀 si ya existe re-escribe 
with open('pagina.html', 'w') as f:
    f.write('hola desde escribirArchivo.py')
    f.write(""" <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>soy un file html</h1>
</body>
</html>""")
    
print('Archivo creado y escrito')

# *Escribir con modo "w"
# 👀 si ya existe re-escribe 
with open('pagina.html', 'a') as f:
    f.write('<div> escrito desde PY </div>')