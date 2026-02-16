from coches import Coche

mi_coche = Coche("Chevrolet", "Aveo", "Azul")
salida = False

while not salida:
    print("\n--- MENÚ COCHE ---")
    print("1. Mostrar información")
    print("2. Acelerar")
    print("3. Frenar")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mi_coche.mostrar_info()

    elif opcion == "2":
        cantidad = int(input("¿Cuánto quieres acelerar? "))
        mi_coche.acelerar(cantidad)

    elif opcion == "3":
        cantidad = int(input("¿Cuánto quieres frenar? "))
        mi_coche.frenar(cantidad)

    elif opcion == "4":
        salida = True
        print("Saliendo del programa...")

    else:
        print("Opción no válida")
