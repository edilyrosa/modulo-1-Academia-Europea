

#& 2. ELIF
# Es una forma de agregar múltiples condiciones a una sentencia if-else. 
#? Ejercicio: Califica a un estudiante según su calificación, 
# con rangos de {
# +90,  -> # Excelente 🥳
# +80,  -> # Muy bien 👏
# +70,  -> # Bien 👍
# +60,  -> # Suficiente 👌
# else -> # Insuficiente 😞
# }

calificacion = -1
if calificacion < 1 or calificacion > 100:
    print("Calificación no válida")
elif calificacion >= 90:
    print("Excelente 🥳")
elif calificacion >= 80:
    print(" Muy bien 👏")
elif calificacion >= 70:
    print("bien 👏")
elif calificacion >= 60:
    print("Suficiente 👌")
else:
    print("Insuficiente 😞")
    
    
print('Fin del elif')