class CuentaBancaria:

    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes.")

    def mostrar_saldo(self):
        print("Titular:", self.titular)
        print("Saldo actual:", self.saldo)
