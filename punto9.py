def calcular_calificacion(nombre, asignatura, nota1, nota2, nota3):
    calificacion_final = (nota1 * 0.30) + (nota2 * 0.30) + (nota3 * 0.40)
    if calificacion_final >= 4.0:
        estado = "Aprobada"
    else:
        estado = "Reprobada"
    print("Nombre del estudiante:", nombre)
    print("Asignatura:", asignatura)
    print("Notas: calificacion 1:", nota1, "calificacion 2:", nota2, "calificacion 3:", nota3)
    print("Calificacion final:", calificacion_final)
    print("El estado de la asignatura es:", estado)

nombre = input("Ingrese el nombre del estudiante: ")
asignatura = input("Ingrese la asignatura: ")

nota1 = float(input("Digite la primera nota (0 a 5):  "))
nota2 = float(input("Digite la segunda nota (0 a 5): "))
nota3 = float(input("Digite la tercera nota (0 a 5): "))

calcular_calificacion(nombre, asignatura, nota1, nota2, nota3)