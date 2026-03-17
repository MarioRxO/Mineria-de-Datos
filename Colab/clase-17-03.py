from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

data = {
    'correo': [
        "gana dinero rapido",
        "oferta exclusiva gratis",
        "reunion de trabajo",
        "invitacion a cenar",
        "felicidades has ganado un premio"
    ],
    'clase': [
        "spam",
        "spam",
        "no spam",
        "no spam",
        "spam"
    ]
}

df = pd.DataFrame(data)

print(df)

#convertir el texto en una matriz de caracteristicas
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(df['correo'])
y = df['clase']

print(x.toarray())

#Variable objetivo
y = df['clase']

#Entrenar el modelo de Naive Bayes
modelo = MultinomialNB()
modelo.fit(x, y)

#Predecir si un correo es spam o no
correo_nuevo = ["gana dinero ahora"]
correo_vectorizado = vectorizer.transform(correo_nuevo)
prediccion = modelo.predict(correo_vectorizado)

print(prediccion)
