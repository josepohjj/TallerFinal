def procesar_notas():
    cantidad_notas = int(input("¿Cuántas notas desea ingresar? "))
    suma_notas = 0
    contador = 0

    while contador < cantidad_notas:
        nota = float(input(f"Ingrese la nota {contador + 1} (0 a 5):"))
        if 0 <= nota <= 5:
            suma_notas += nota
            contador += 1
        else:
            print("La nota debe estar entre 0 y 5. Intenta de nuevo.")

    promedio = suma_notas / cantidad_notas

    print(f"El promedio del estudiante es: {promedio}")

    if promedio >= 4.5:
        print("Estudiante aprobado.")
    else:
        print("Estudiante reprobado.")

procesar_notas()
