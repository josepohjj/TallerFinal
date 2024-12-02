def jubilacion(sexo, edad):
    if sexo == "hombre":
        if edad >= 63:
            print("Ya puede jubilarse.")
        else:
            print("Aun no puede jubilarse.")
    elif sexo == "mujer":
        if edad >= 54:
            print("Ya puede jubilarse.")
        else: 
            print("Aun no puede jubilarse.")
sexo = input("Ingrese su sexo (hombre/mujer): ")
edad = int(input("Ingrese su edad: "))

jubilacion(sexo, edad)