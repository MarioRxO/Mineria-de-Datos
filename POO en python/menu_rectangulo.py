from rectangulos import Rectangulo

ancho = float(input("Ingresa el ancho: "))
alto = float(input("Ingresa el alto: "))

mi_rect = Rectangulo(ancho, alto)

salida = False

while not salida:
    print("\n--- MENÚ RECTÁNGULO ---")
    print("1. Mostrar información")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mi_rect.mostrar_info()

    elif opcion == "2":
        salida = True
        print("Saliendo...")

    else:
        print("Opción inválida")
