# Ejercicio 1

N = int(input("Introduce un numero: "))
suma = 0

for i in range(1, N + 1):
    suma += i

print(f"Las suma de los primeros numeros {N} es: {suma}")
# Ejercicio 2

num = int(input("Introduce un numero: "))
i = 0

for i in range(1, num + 1):
    i *= i

print(f"El factorial de {num} es: {i}")

# Ejercicio 3

tabla= int(input("Introduce un numero: "))

for i in range(1, 11):
    resultado = tabla * i
    print(f"{tabla} x {i} = {resultado}")


suma_notas = 0
contador = 0

print("Ingresa las notas (introduce un número negativo para finalizar):")

# Ejercicio 4
for _ in range(1000): 
    nota = float(input(f"Nota {contador + 1}: "))
    if nota < 0:
        break
    suma_notas += nota
    contador += 1

if contador > 0:
    promedio = suma_notas / contador
    print(f"El promedio de las {contador} notas es: {promedio:.2f}")
else:
    print("No se ingresaron calificaciones validas")


 #Ejercicio 5
    base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))
resultado = 1

for _ in range(exponente):
    resultado *= base

print(f"El resultado de {base}^{exponente} es: {resultado}")

#Ejercicio 6
a = int(input("Valor inicial (A): "))
b = int(input("Valor final (B): "))
suma_pares = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        suma_pares += i

print(f"La suma de los números pares entre {a} y {b} es: {suma_pares}")