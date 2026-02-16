class Coche:

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, velocidad):
        if velocidad > 0:
            self.velocidad += velocidad

    def frenar(self, velocidad):
        if velocidad > 0:
            self.velocidad -= velocidad
            if self.velocidad < 0:
                self.velocidad = 0

    def mostrar_info(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Velocidad actual:", self.velocidad)
