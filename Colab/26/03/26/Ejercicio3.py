import numpy as np
from scipy import stats

#1) Datos
pesos = np.array([
    495,498,502,490,497,499,
    501,493,496,498,492,495,500,494,496])

#2) Hipotesis
mu_0 = 500

#3) Ejecuta la prueba t de 1 muestra
res = stats.ttest_1samp(pesos, mu_0)

#4) Extrae el estadistio t y el p-value
print("t:", res.statistic)
print("p-value:", res.pvalue)

#5) Decisión

alpha = 0.05

if res.pvalue < alpha:
    print("Rechazamos H0")
else:
    print("No rechazamos H0")