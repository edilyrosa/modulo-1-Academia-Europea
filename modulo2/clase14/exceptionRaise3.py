def valida_edad(edad):
    if edad < 18: #para mi es un problema que sea menor de edad
        raise ValueError("❌La edad debe ser mayor o igual a 18, ERES UN BEBE")
    return 'Edad válida 👱🏽‍♂️'

try:
    print(valida_edad(18))
except ValueError as e:
    print(e, type(e))