num = int(input("Introduce un número: "))
if num % 2 == 0:
    print("Es par")
else:
    print("Es impar")

num = int(input("Ïntroduce un numero mayor o menor a 0: "))
if num > 0:
    print("Positivo")
elif num < 0:
    print("Ngativo")


num = int(input("Ïntroduce tu edad: "))
if num > 17:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

num = int(input("Ïntroduce tu calificacion":  ))
if num >= 60:
    print("Aprobaste")
else:
    print("Reprobaste")

num = int(input("Ïntroduce tu calificacion: "))
if num >= 90:
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("B")
elif num>= 60:
    print("C")
else:
    print("D")

temperatura = int(input("Ïntroduce la temperatura: "))
if temperatura < 0:
    estado = "Sólido"
elif 0 <= temperatura <= 100:
    estado = "Líquido"
else:
    estado = "Vapor"

print(f"El estado del agua es: {estado}")