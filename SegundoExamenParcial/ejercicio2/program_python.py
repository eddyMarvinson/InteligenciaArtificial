# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:02:28 2020

@author: edson
"""
import random
import math
import pandas as pd
# funcion evaluadora f(x) = x^3 + x^2 + x
def funcion_evaluadora(x):
    ans = []
    for value in x:
        ans.append(pow(value, 3) + pow(value, 2) + value)
    return ans
# funcion conversion decimal - binario cadena con k bits
def decimal_binario(x, k):
    ans = []
    for value in x:
        tmp = str(int(bin(value)[2:]))
        tmp = tmp[::-1]
        while len(tmp) < k:
            tmp = tmp + '0'
        tmp = tmp[::-1]
        ans.append(tmp)
    return ans
# funcion binario a decimal
def bin_decimal(x):
    ans = []
    for value in x:
        suma = 0
        pw = 0
        for ch in value:
            if ch == '1':
                suma += pow(2, pw)
            pw += 1
        ans.append(suma)
    return ans
# funcion mezcla resultado mezcla(0000,1111) = 0011
def mezcla(i, j, k):
    return i[0:k] + j[k:len(j)]
# funcion conversion de los valores de un arreglo a negativos
def lista_negativa(x):
    ans = []
    for i in x:
        ans.append(-i)
    return ans
# generando la serie para el cruce tomando en potencias de dos
def serie(k, m):
    s = []
    n = pow(2, k) // 2
    value = n * 2 - 1
    for i in range(0, n):
        s.append(value)
        value -= 2
    while len(s) < m:
        r = lista_negativa(s[::-1])
        s = s + r
    return s
# funcion para la seleccion de adversarios
def seleccion(x, k):
    pareja = serie(k, len(x))
    ans = []
    for i in range(0, len(x)):
        ans.append(mezcla(x[i], x[i + pareja[i]], len(x[i]) // 2))
    return ans
# selecciona al mejor
def mutacion(x, fx, y, fy):
    ans = []
    for i in range(0, len(x)):
        if(fx[i] > fy[i]):
            ans.append(x[i])
        else:
            ans.append(y[i])
    return ans
# creando lista de enteros aleatorios
# tamaño de la muestra debe ser potencia de dos para el torneo
tamaño_muestra = 16
max_gen = int(math.log2(tamaño_muestra)) + 1
data = pd.DataFrame(columns=('x', 'fx', 'binario', 'cruce', 'cruce_decimal', 'f_cruce', 'mutacion'))
x = random.sample(range(pow(2, max_gen)), tamaño_muestra)
# generaciones
for generacion in range(1, max_gen):
    data['x'] = x
    data['fx'] = funcion_evaluadora(x)
    data['binario'] = decimal_binario(x, max_gen)
    data['cruce'] = seleccion(data['binario'], generacion)
    data['cruce_decimal'] = bin_decimal(data['cruce'])
    data['f_cruce'] = funcion_evaluadora(data['cruce_decimal'])
    data['mutacion'] = mutacion(data['x'], data['fx'], data['cruce_decimal'], data['f_cruce'])
    x = data['mutacion']
    print(data)
    #print("===============================================================")