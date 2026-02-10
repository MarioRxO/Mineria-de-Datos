print("Hola, Mundo!")

numero = 10.5
texto = "Este es un texto"
verdadero = True
falso = False
print(numero)

mi_lista = [1,2,3,4]
print(mi_lista[3])

#Diccionario
mi_diccionario = {
    "Nombre": "Juan",
    "Edad": 40,
    "Ciudad": "Madrid"
    }
print(mi_diccionario["Edad"])

#Operadores
suma = 5+5
resta = 5-4
multi = 5*5
divi = 10/2 #resultado
modulo = 10%2 #residuo

# Operadores Logico
# and , or , not

#Estructuras de control condicionales
a = 10
if a > 0:
    print("Positivo")
elif a < 0:
    print("Ngativo")
else:
    print("El numero es negativo")

#match case
color = "rojo"

match color:
    case "verde":
        print("Verde")
    case "rojo":
        print("Rojo")
    case _: #El deafult de py
        print("No hay color")

#funcion
def sumar(a,b):
    return a + b

print(sumar(1,5))

#Bucles
animales = ["perro","gato","raton","oveja"]

for animal in animales:
    print(animal)

for i in range(2,20,2):
    print(i)