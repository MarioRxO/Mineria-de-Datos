import numpy as np
import scipy.stats as stats
import pandas as pd 

# Datos
nu_0 = 10
n = 49
x_barra = 9.7
s = 0.5
alpha = 0.01

# Estadístico t
t = (x_barra - nu_0) / (s / np.sqrt(n))

# Valor crítico (cola izquierda)
t_critical = stats.t.ppf(alpha, df=n-1)

# Decisión
if t < t_critical:
    print("Rechazamos la hipótesis nula")
else:
    print("No rechazamos la hipótesis nula")

print("t calculado:", t)
print("t crítico:", t_critical)

df = pd.DataFrame({
    'Parametros':['Media Teorica','Media Muestral','Desviación Estándar','n','alpha'],
    'Valores':[nu_0, x_barra, s, n, alpha]
})

print(df)