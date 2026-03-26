import numpy as np
from scipy import stats


#1) Datos
A = np.array([12.5, 13.2, 12.8, 14.0, 13.5, 12.9, 13.1])
B = np.array([14.2, 15.0, 14.8, 13.9, 15.5, 14.7, 15.1])

#2) Hipotesis

#3) Ejecuta la prueba t de 2 muestras independientes
res = stats.ttest_ind(A, B)

#4) Extrae el estadistio t y el p-value
print("t:", res.statistic)
print("p-value:", res.pvalue)


alpha = 0.05

#5) Decisión
if res.pvalue < alpha:
    print("Sí hay diferencia")
else:
    print("No hay diferencia")