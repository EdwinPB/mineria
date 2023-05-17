from config import *
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import linear_model
# import json

#LECTURA DE DATOS
datos = pd.read_csv('data.csv',sep=';')
dataframe = pd.DataFrame(datos)
for i in dataframe["fixed acidity"]:
        if i.__contains__(','):
                new_value = i.replace(",", ".")
                dataframe = dataframe.replace({ 'fixed acidity': { i: new_value }})
dataframe['fixed acidity'] = dataframe['fixed acidity'].astype(float)

for i in dataframe["volatile acidity"]:
        if i.__contains__(','):
                new_value = i.replace(",", ".")
                dataframe = dataframe.replace({ 'volatile acidity': { i: new_value }})
dataframe['volatile acidity'] = dataframe['volatile acidity'].astype(float)

for i in dataframe["citric acid"]:
        if i.__contains__(','):
                new_value = i.replace(",", ".")
                dataframe = dataframe.replace({ 'citric acid': { i: new_value }})
dataframe['citric acid'] = dataframe['citric acid'].astype(float)

for i in dataframe["residual sugar"]:
        if i.__contains__(','):
                new_value = i.replace(",", ".")
                dataframe = dataframe.replace({ 'residual sugar': { i: new_value }})
dataframe['residual sugar'] = dataframe['residual sugar'].astype(float)

for i in dataframe["chlorides"]:
        if i.__contains__(','):
                new_value = i.replace(",", ".")
                dataframe = dataframe.replace({ 'chlorides': { i: new_value }})
dataframe['chlorides'] = dataframe['chlorides'].astype(float)

for i in dataframe["free sulfur dioxide"]:
        if i.__contains__(','):
                new_value = i.replace(",", ".")
                dataframe = dataframe.replace({ 'free sulfur dioxide': { i: new_value }})
dataframe['free sulfur dioxide'] = dataframe['free sulfur dioxide'].astype(float)

for i in dataframe["total sulfur dioxide"]:
        if i.__contains__(','):
                new_value = i.replace(",", ".")
                dataframe = dataframe.replace({ 'total sulfur dioxide': { i: new_value }})
dataframe['total sulfur dioxide'] = dataframe['total sulfur dioxide'].astype(float)

for i in dataframe["density"]:
        if i.__contains__(','):
                new_value = i.replace(",", ".")
                dataframe = dataframe.replace({ 'density': { i: new_value }})
dataframe['density'] = dataframe['density'].astype(float)

for i in dataframe["pH"]:
        if i.__contains__(','):
                new_value = i.replace(",", ".")
                dataframe = dataframe.replace({ 'pH': { i: new_value }})
dataframe['pH'] = dataframe['pH'].astype(float)

for i in dataframe["sulphates"]:
        if i.__contains__(','):
                new_value = i.replace(",", ".")
                dataframe = dataframe.replace({ 'sulphates': { i: new_value }})
dataframe['sulphates'] = dataframe['sulphates'].astype(float)

for i in dataframe["alcohol"]:
        if i.__contains__(','):
                new_value = i.replace(",", ".")
                dataframe = dataframe.replace({ 'alcohol': { i: new_value }})
dataframe['alcohol'] = dataframe['alcohol'].astype(float)

print (dataframe.info())
print (dataframe.head())

X = (dataframe[["pH","sulphates","alcohol"]])
y = (dataframe["quality"])

#Entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42)

model = LogisticRegression(solver='lbfgs', max_iter=10000)
model.fit(X_train,y_train)
print ("------2")
datanew = {
        'pH':[3.0, 2],
        'sulphates':[0.10, 0.90],
        'alcohol':[2.5, 4.6]}

#nuevo cliente
clientesnew = pd.DataFrame(datanew,columns=['pH','sulphates','alcohol'])
print ("------3")
prediccion = model.predict(clientesnew)
print ("------4")
print("result---->", model.predict(clientesnew))
print("result---->", model.predict(clientesnew))
print("result---->", model.predict(clientesnew))
print("result---->", model.predict(clientesnew))
print("result---->", model.predict(clientesnew))
print("result---->", model.predict(clientesnew))
print("result---->", model.predict(clientesnew))
print("result---->", model.predict(clientesnew))
print("result---->", model.predict(clientesnew))
print("result---->", model.predict(clientesnew))




















#Extracion de datos.
# cur.execute('SELECT * FROM tvino ')
# datos=cur.fetchall()
# #Convertir los datos a diccionario
# columnNames = [column[0] for column in cur.description]
# print(columnNames)
# for i in range(0,10):
#     print(i)
#     if i  >= 10:
#         break
#     i += i + 1   
# print(type (datos))

# array = np.array(datos)
# cantidad= len (array)
# print (array[cantidad-1])

# jsondata = json.dumps(datos)
# print (jsondata)
# print (type (jsondata))

# print(array[0][0])
# dataframe = pd.DataFrame(datos)
# print(dataframe)
