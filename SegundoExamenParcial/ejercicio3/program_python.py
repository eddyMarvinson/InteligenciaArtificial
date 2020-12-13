# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:11:59 2020

@author: edson
"""
import pandas as pd
import numpy as np
# nombres para las columnas
_names = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16']
# Importando dataset y separando en dos dataset
data=pd.read_csv('data/crx.data', names=_names)
data_size = len(data.index)
train_size = int(data_size * 0.8)
train_file = data.iloc[0:train_size]
test_file = data.iloc[train_size:data_size - 1]
train_file.to_csv('train.csv', index=False)
test_file.to_csv('test.csv', index=False)
# Importando test y train
data_train=pd.read_csv('train.csv')
data_test=pd.read_csv('test.csv')
# Reemplazando valores nulos ? por valores nan 
data_train=data_train.replace('?',np.nan)
data_test=data_train.replace('?',np.nan)
# Eliminando filas que contengan valores nulos
data_train.dropna(inplace=True)
data_test.dropna(inplace=True)
# Asignando valores numericos a valores alfabeticos
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
# Datos de entrenamiento
data_train['A1']=encoder.fit_transform(data_train.A1.values)
data_train['A4']=encoder.fit_transform(data_train.A4.values)
data_train['A5']=encoder.fit_transform(data_train.A5.values)
data_train['A6']=encoder.fit_transform(data_train.A6.values)
data_train['A7']=encoder.fit_transform(data_train.A7.values)
data_train['A9']=encoder.fit_transform(data_train.A9.values)
data_train['A10']=encoder.fit_transform(data_train.A10.values)
data_train['A12']=encoder.fit_transform(data_train.A12.values)
data_train['A13']=encoder.fit_transform(data_train.A13.values)
data_train['A16']=encoder.fit_transform(data_train.A16.values)
# Datos de prueba
data_test['A1']=encoder.fit_transform(data_test.A1.values)
data_test['A4']=encoder.fit_transform(data_test.A4.values)
data_test['A5']=encoder.fit_transform(data_test.A5.values)
data_test['A6']=encoder.fit_transform(data_test.A6.values)
data_test['A7']=encoder.fit_transform(data_test.A7.values)
data_test['A9']=encoder.fit_transform(data_test.A9.values)
data_test['A10']=encoder.fit_transform(data_test.A10.values)
data_test['A12']=encoder.fit_transform(data_test.A12.values)
data_test['A13']=encoder.fit_transform(data_test.A13.values)
data_test['A16']=encoder.fit_transform(data_test.A16.values)
# Asignando valores de las columnas
X_train=data_train[['A1','A4','A5','A6','A7','A9','A10','A12','A13']]
y_train=data_train['A16'] 
X_test=data_test[['A1','A4','A5','A6','A7','A9','A10','A12','A13']]
y_test=data_test['A16'] 
# Transformando valores
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(X_train)
X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)
# Creando y entrenando la red neuronal mlp
from sklearn.neural_network import MLPClassifier
mlp=MLPClassifier(hidden_layer_sizes=(6,6,6),solver='lbfgs',max_iter=6000)
mlp.fit(X_train, y_train)
y_pred = mlp.predict(X_test)
# Realizando un reporte de la clasificacion
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
# Creando la matriz de confusion con datos de prueba y datos predecidos
from sklearn.metrics import confusion_matrix
confmat = confusion_matrix(y_test, y_pred)
print("matrix_conf\n",confmat)
print(pd.crosstab(y_test, y_pred, rownames=['Verdaderos'],colnames=['Prediccion'],margins=True))