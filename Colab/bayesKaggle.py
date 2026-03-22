import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("Customer_support_data.csv")
# Extract relative columns and rename them
df = df[["Customer Remarks", "CSAT Score"]].rename(columns={"Customer Remarks": "texto", "CSAT Score": "sentimiento"})
# Drop missing text rows to prevent CountVectorizer errors
df = df.dropna(subset=["texto"])

print(df.head())

#contamos el numero de palabas en cada rato
print(df['sentimiento'].value_counts())

#Crear el modelo de Naive Bayes Multimodal
vectorizar = CountVectorizer()
X = vectorizar.fit_transform(df['texto'])
y = df['sentimiento']

#creamos el modelo
modelo = MultinomialNB()
modelo.fit(X, y)

#hacemos predicciones
ejemplos = ["i hate this product,it's terrible", "this is the best product i have ever used", "it's okay, not bad but not great"]
X_ejemplos = vectorizar.transform(ejemplos)
predicciones = modelo.predict(X_ejemplos)

print(predicciones)

#Evaluar el modelo
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
modelo.fit(x_train, y_train)

y_pred = modelo.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
