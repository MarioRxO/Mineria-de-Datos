class Rectangulo:

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

    def mostrar_info(self):
        print("Ancho:", self.ancho)
        print("Alto:", self.alto)
        print("Área:", self.calcular_area())
        print("Perímetro:", self.calcular_perimetro())
