import numpy as np
from scipy import stats

#1) DAtos: calificaciones registradas de los studiante
scores = np.array([
    72,68,75,70,66,74,71,69,73,67,
    70,72,65,76,68,71,69,74,70,66,
    73,67,72,68,75,69,71,70,74,86

])

#2) Hipotesis
mu_0 = 85

#3) Ejecuta la prueba t de 1 muestra
res = stats.ttest_1samp(scores, mu_0)

#4) Extrae el estadistio t y el p-value

t_stat = res.statistic
p_value = res.pvalue

#5 Defina el nivel de significacncia
alpha = 0.05

#6) Decisw ai rechZ H0
print(" t:", t_stat)
print("P-value:", p_value)

if p_value < alpha:
    print("Rechazamos la hipotesis nula")
else:
    print("No rechazamos la hipotesis nula")