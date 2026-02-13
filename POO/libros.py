#Crear sistema para gestionar una biblioteca con las siguientes clases:Libro, Ususario, iblioteca
class Libro:

    def __init__(self):
        self.id = "1234"
        self.titulo = "Supremacia cuantica"
        self.autor  =   "Michio kaku"
        self.publicacion = "2004"
        self.disponible = True

    #Metodos

    def mostrar_informacion(self,id):
        self.id = id
        if self.id == "1234":
            print(f"Titulo: {self.titulo} Autor: {self.autor} Año: {self.publicacion} Disponible: {self.disponible}")
        else:
            print("El codigo no existe")

    def prestar_libro(self, id):
        self.id = id
        if self.id == "1234":
            if self.disponible:
                print("Libro disponible-El libro de puede prestar")
                self.disponible = False
            else:
                print("Libro no disponible")
        
    def devolver_libro(self,id):
        self.id = id
        if self.id == "1234" and self.disponible == False:
            if self.disponible:
                print("Libro ya prestado")
                self.disponible = False
            else:
                print("Libro devuleto")