import math
import pandas as pd
import numpy as np
from scipy import stats
import collections
import matplotlib.pyplot as plt

# inciso a
dataFile = pd.read_csv("alumno.csv")
listaNotaPromedio = dataFile["NotaPromedio"]

def media(x):
	sum_i = 0
	N = len(x)
	for x_i in x:
		sum_i += x_i
	sum_i /= N
	return sum_i

print("Media: %.2f" %media(listaNotaPromedio))

def desviacionEstandar(x):
	sum_i = 0
	N = len(x) - 1
	X_media = media(x)
	for x_i in x:
		sum_i += (x_i - X_media) * (x_i - X_media)
	sum_i /= N
	sum_i = math.sqrt(sum_i)
	return sum_i

print("Desviacion Estandar: %.2f" %desviacionEstandar(listaNotaPromedio))

# comment inciso a

# inciso b

# mediante pandas
print("::Mediante pandas::")
listaNotaPromedio = dataFile["NotaPromedio"].mean()
listaSexoModa = dataFile["Sexo"].mode()
print("Media: %.2f" %listaNotaPromedio)
print("Moda: %.2f" %listaSexoModa)

# mediante numpy
print("::Mediante numpy y stats::")
listaNotaPromedio = np.mean(dataFile["NotaPromedio"])
listaSexoModa = stats.mode(dataFile["Sexo"])
print("Media: %.2f" %listaNotaPromedio)
print(listaSexoModa)

# inciso c
def graficar1(dataF):
	tmp = collections.Counter(dataF)
	x = list(set(dataF))
	y = []
	for x_i in x:
		y.append(tmp[x_i])
	plt.bar(x, y)
	plt.show()

def graficar2(dataF):
	tmp = collections.Counter(dataF)
	x = list(set(dataF))
	y = []
	for x_i in x:
		y.append(tmp[x_i])
	plt.bar(x, y, align = 'center', width = 6)
	mean = dataF.mean()
	median = dataF.median()
	std = dataF.std()
	plt.axvline(mean, color='r', linestyle='--')
	plt.axvline(median, color='g', linestyle='--')
	plt.axvline(std, color='b', linestyle='--')
	plt.show()

#graficar1(dataFile["Departamento"])
graficar2(dataFile["NotaPromedio"])

# commentarios
# Otra forma de obtener listas
# dataFile = pd.read_csv("alumno.csv", skiprows=1, names=["CI","NombreCompleto","Sexo","Departamento","NotaPromedio","Edad"])
# listaNotaPromedio = dataFile.NotaPromedio.tolist()