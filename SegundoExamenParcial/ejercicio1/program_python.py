# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 21:24:39 2020

@author: edson
"""
import json
import numpy
import pandas
import random
# abriendo el archivo que contiene los datos del grafo
with open("data/grafo17.json", "r") as tsp_data:
    tsp = json.load(tsp_data)
# asignando valores matriz de adyacencia y numero de nodos
distance_map = tsp["DistanceMatrix"]
IND_SIZE = tsp["TourSize"]
# Funcion de evaluacion de Tour
def evalTSP(individual):
    distance = distance_map[individual[-1]][individual[0]]
    for gene1, gene2 in zip(individual[0:-1], individual[1:]):
        distance += distance_map[gene1][gene2]
    return distance
# Funcion para cruzar dos cromosomas
def cruceCX(ind1, ind2):
    size = min(len(ind1), len(ind2))
    p1, p2 = [0] * size, [0] * size
    for i in range(size):
        p1[ind1[i]] = i
        p2[ind2[i]] = i
    cxpoint1 = random.randint(0, size)
    cxpoint2 = random.randint(0, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else:
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1
    for i in range(cxpoint1, cxpoint2):
        temp1 = ind1[i]
        temp2 = ind2[i]
        ind1[i], ind1[p1[temp2]] = temp2, temp1
        ind2[i], ind2[p2[temp1]] = temp1, temp2
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]
    return ind1, ind2
# Eliminar ultimo elemento de un arreglo
def pop_back(z):
    z = list(z)
    value = z.pop()
    return numpy.array(z), value
# Eliminar priemr elemento de un arreglo
def pop_front(z):
    z = list(z)
    value = z.pop()
    return numpy.array(z), value
# Agregar un elemento a un arreglo
def push_back(z, value):
    z = list(z)
    z.append(value)
    return numpy.array(z)
# programa pricipal
def main():
    # Generando poblacion aleatoria
    # Tamaño de la poblacion
    poblacionSize = 30
    poblacion = []
    for item in range(poblacionSize):
        arreglo_aleatorio = numpy.array([i for i in range(IND_SIZE)])
        random.shuffle(arreglo_aleatorio)
        poblacion.append(arreglo_aleatorio)
    poblacion = numpy.array(poblacion)
    a = []
    b = []
    c = []
    arreglo_optimo = numpy.array([i for i in range(IND_SIZE)])
    random.shuffle(arreglo_optimo)
    # Numero de generaciones
    num_gen = 20
    # Eliminacion por Generacional seleccionando hijos aptos
    for gen in range(num_gen):
        poblacion_nueva = []
        mejor_generacion = arreglo_optimo
        while len(poblacion) > 1:
            poblacion, arreglo1 = pop_front(poblacion)
            poblacion, arreglo2 = pop_back(poblacion)            
            cruce1, cruce2 = cruceCX(arreglo1, arreglo2)
            poblacion_nueva.append(cruce1)
            poblacion_nueva.append(cruce2)
            # guardando mejor cruce
            if evalTSP(cruce1) < evalTSP(mejor_generacion):
                mejor_generacion = cruce1
            if evalTSP(cruce2) < evalTSP(mejor_generacion):
                mejor_generacion = cruce2
        arreglo_optimo = mejor_generacion
        poblacion = numpy.array(poblacion_nueva)
        a.append(len(poblacion))
        b.append(evalTSP(arreglo_optimo))
        c.append(arreglo_optimo)    
    return b, arreglo_optimo, evalTSP(arreglo_optimo)
if __name__ == "__main__":    
    data = pandas.DataFrame()
    data['min_generacion'], tour, valor = main()
    print(data)
    print("Tour:", tour)
    print("Min_value:", valor)