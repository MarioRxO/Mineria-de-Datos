import numpy as np
from scipy import stats

#1) Datos
tiempos = np.array([44, 47, 46, 43, 45, 48, 44, 46, 47, 45,
                    44, 46, 45, 43, 47, 48, 44, 46, 45, 47,
                    44, 46, 45, 47, 46])

#2) Hipotesis
mu_0 = 45

#3) Ejecuta la prueba t de 1 muestra
res = stats.ttest_1samp(tiempos, mu_0)

#4) Extrae el estadistio t y el p-value

print("t:", res.statistic)
print("p-value:", res.pvalue)

alpha = 0.05

if res.pvalue < alpha:
    print("Rechazamos H0")
else:
    print("No rechazamos H0")