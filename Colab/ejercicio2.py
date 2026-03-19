import pandas as pd

data = {
    "Fruta": ["Manzana", "Manzana", "Manzana", "Naranja", "Naranja", "Naranja"],
    "Color": ["Rojo", "Rojo", "Rojo", "Naranja", "Naranja", "Naranja"],
    "Peso": [150, 155, 160, 130, 135,140],
    'Textura': [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)
print(df)

#convertimos las variables categoricas a numericas
df['Color'] = df['Color'].map({'Rojo':0, 'Naranja':1})

#convertimos la variable objetivo a numerica
df['Fruta'] = df['Fruta'].map({'Manzana':0, 'Naranja':1})
print(df)

x = df[['Color','Peso','Textura']]
y = df['Fruta']

#Entrenamos el modelo Bayes Gaussiano
modelo = GaussianNB()
modelo.fit(x, y)

#Hacemos una prediccion
nuevo = [[0,140,0]]
prediccion = modelo.predict(nuevo)
print(prediccion)

if prediccion[0] == 0:
    print("La fruta es Manzana")
else:
    print("La fruta es Naranja")

#Evaluar la modelo ocn los datos de entranmiento
y_pred = modelo.predict(x)
accuracy = accuracy_score(y, y_pred)
print(f"Presicion: {accuracy}")