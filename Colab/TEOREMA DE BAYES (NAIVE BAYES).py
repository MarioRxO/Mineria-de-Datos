from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

data = {
    'resena': [
        "el producto funciona excelente",
        "muy buena calidad",
        "el producto llego dañado",
        "muy mala calidad",
        "excelente producto y calidad",
        "mal servicio y mal producto",
        "pésimo producto, no funciona"
    ],
    'clasificacion':[
        "satisfecho",
        "satisfecho",
        "insatisfecho",
        "insatisfecho",
        "satisfecho",
        "insatisfecho",
        "insatisfecho"
    ]
}

df = pd.DataFrame(data)

print(df)

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(df['resena'])
y = df['clasificacion']

print(x.toarray())

modelo = MultinomialNB()
modelo.fit(x, y)

resena_nueva = ["producto mala calidad"]
resena_vectorizada = vectorizer.transform(resena_nueva)
prediccion = modelo.predict(resena_vectorizada)

print(prediccion)
