# Para tributar un determinado impuesto se debe ser mayor de 16 años y
# tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un
# programa que pregunte al usuario su edad y sus ingreso mensuales y muestre
# por pantalla si el usuario tiene que tributar o no.

edad = int(input("Edad: "))
if edad > 16:
    ingresos = float(input("Ingresos mensuales: "))
    if ingresos >= 1000:
        print("Usted tiene que tributar impuestos.")
    else:
        print("Usted no tiene que tributar impuestos.")
else:
    print("Usted no es mayor de 16 años.")        