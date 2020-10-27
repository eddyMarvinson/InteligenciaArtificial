import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn import preprocessing

dataFile = pd.read_csv("mitbih_test.csv")

print("matrix")
print(dataFile)

imputation = SimpleImputer(missing_values=np.nan, strategy="mean")
matrix_imputer = imputation.fit_transform(dataFile)
print("matrix imputer")
print(matrix_imputer)

matrix_normalize = preprocessing.normalize(matrix_imputer)
print("matrix normalize")
print(matrix_normalize)
