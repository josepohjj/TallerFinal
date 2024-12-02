def conversion(dolares, tasa_cambio):
    return dolares * tasa_cambio
tasa_cambio = 3934
seguir = "si"

while seguir == "si": 
    dolares = float(input("Cantidad de dolares: "))
    
    pesos = conversion(dolares, tasa_cambio)
    print(dolares, "Dolares equivalen a", pesos, "pesos")

    seguir = input("¿Quiere continuar con las conversiones? (si/no): ")
print("Gracias por usar nuestra aplicacion.")