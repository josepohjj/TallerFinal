def pago(precio):
    if precio > 20000:
        descuento = precio * 0.20
        precio_final = precio - descuento
        print("El precio original es:", precio)
        print("Se aplica un descuento de:", descuento)
        print("El precio final a pagar es:", precio_final)
    else:
        print("El precio original es", precio, "asi que no habra descuento")

precio = float(input("Precio del producto: "))

pago(precio)