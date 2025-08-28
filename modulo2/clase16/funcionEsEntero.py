

def es_entero():
    try:
        int(input("Ingrese un número: "))
        return True  # Aquí sí se sale porque el valor es válido
    except ValueError:
        return False

# Uso
if es_entero():
    print("✅ Se ingresó un número entero válido.")
else: 
    print("❌ NO ingresó un número entero.")

# No es posible probarlo directamente mediante 
# tests unitarios sin técnicas como "mockear" la función input(), porque esa función espera 
# interacción real del usuario en consola.
