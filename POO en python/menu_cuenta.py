from cuentas import CuentaBancaria

mi_cuenta = CuentaBancaria("Mario")
salida = False

while not salida:
    print("\n--- MENÚ CUENTA BANCARIA ---")
    print("1. Mostrar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mi_cuenta.mostrar_saldo()

    elif opcion == "2":
        cantidad = float(input("Cantidad a depositar: "))
        mi_cuenta.depositar(cantidad)

    elif opcion == "3":
        cantidad = float(input("Cantidad a retirar: "))
        mi_cuenta.retirar(cantidad)

    elif opcion == "4":
        salida = True
        print("Saliendo...")

    else:
        print("Opción inválida")
