import pandas as pd

datos = {
    "Nombre": ["Ana","Luis","Maria","Juan"],
    "Edad": [20,22,19,21],
    "Calificacion": [85,90,78,88]
}

df = pd.DataFrame(datos)
print("Tabla completa")
print(df)

print("\n Promerdio")
print(df["Calificacion"].mean())