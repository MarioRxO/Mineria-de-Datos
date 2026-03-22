# Parte 0

import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Parte 1: Exploración de datos

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "amazon_cells_labelled.txt")

df = pd.read_csv(file_path, 
                 sep="\t", 
                 header=None, 
                 names=["sentence","label"])

print("Primeras filas:")
print(df.head())

print("Información del dataset:")
print(df.info())

print("Distribución de clases:")
print(df["label"].value_counts())

# Parte 2: Representación del texto

X = df["sentence"]
y = df["label"]

vectorizer = CountVectorizer()

X_vectorized = vectorizer.fit_transform(X)

print("\nNúmero de palabras en el vocabulario:")
print(len(vectorizer.vocabulary_))

# Parte 3: Modelo Naive Bayes Multinomial

model = MultinomialNB()

# Parte 4: Predicciones

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Entrenar modelo
model.fit(X_train, y_train)

# Predicciones
y_pred = model.predict(X_test)

# Parte 5: Evaluación del modelo (división)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:")
print(accuracy)

print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred))

# Parte 6: Entrenamiento y métricas

print("Reporte de clasificación:")
print(classification_report(y_test, y_pred))

# Prueba manual

test_sentences = [
    "This product is amazing",
    "Worst purchase ever",
    "I really like this phone",
    "Terrible quality"
]

test_vectors = vectorizer.transform(test_sentences)

predictions = model.predict(test_vectors)

print("Predicciones nuevas:")
for sentence, pred in zip(test_sentences, predictions):
    print(sentence, "->", "Positivo" if pred == 1 else "Negativo")  