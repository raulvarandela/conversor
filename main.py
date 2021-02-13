"""
@author: Raúl Varandela Marra
Date: 13/02/2021
"""

opcion = 0

while True:

    print("Selecciona que conversión quieres realizar: ")
    print()
    print("De Kg a Libras ................................ 1")
    print("De Libras a Kg ................................ 2")
    print("De cm a pulgadas .............................. 3")
    print("De pulgadas a cm .............................. 4")
    print("Salir ......................................... 5")
    print()

    opcion = input("Selecciona una opción: ")
    print()

    if (opcion == "1"):
        valor = int(input("Introduce una cantidad a convertir: "))
        print(f"La conversión de {valor} Kg a Libras es de {valor * 2, 205}")
    elif (opcion == "2"):
        valor = int(input("Introduce una cantidad a convertir: "))
        print(f"La conversión de {valor} Libras a Kg es de {valor / 2, 205}")
    elif (opcion == "3"):
        valor = int(input("Introduce una cantidad a convertir: "))
        print(f"La conversión de {valor} cm a pulgadas es de {valor / 2, 54}")
    elif (opcion == "4"):
        valor = int(input("Introduce una cantidad a convertir: "))
        print(f"La conversión de {valor} pulgadas a cm es de {valor * 2, 54}")
    elif (opcion == "5"):
        break
    else:
        print("No se ha seleccionado ninguna opción correcta.")
    print()

print("Saliendo....Adiós :(")