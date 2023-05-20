# 2-devuelve al controlador la informacion solicitada
# aqui van todas las validaciones de la base de dato
from config import *
from flask import Flask, render_template,request,redirect,url_for,flash,session
# pip install pyjwt
import jwt
#
from datetime import datetime,timedelta
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import linear_model
#LECTURA DE DATOS
datos = pd.read_csv('data.csv',sep=';')
dataframe = pd.DataFrame(datos)

class model():
    def m_verificar_admin_usuario(self):
        cur.execute('SELECT username FROM tadmin ')
        usersadmin=cur.fetchall()
        cur.execute('SELECT clave FROM tadmin ')
        claveadmin=cur.fetchall()
        if request.method == 'POST':
            Username=request.form['username']
            Clave=request.form['password']
            i= len(usersadmin)
            global c
            c = 0
            while(c<i):
                if(usersadmin[c][0]==Username and  claveadmin[c][0]==Clave):
                    return "logeado"
                else:
                    c+=1              
            return "noregistrado"        
    def m_crear_token_admin_usuario(self):
        llave ='mysecretkey'
        id_usuarioadmin= self.m_devolver_id_admin_usuario()
        ##timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
        return jwt.encode({'public_id': id_usuarioadmin,
                            'exp': datetime.utcnow()+timedelta(hours=1)
                            },
                            llave)

    def m_devolver_id_admin_usuario(self):
        cur.execute('SELECT id FROM tadmin ')
        idadmin=cur.fetchall()
        cur.execute('SELECT username FROM tadmin ')
        usersadmin=cur.fetchall()
        cur.execute('SELECT clave FROM tadmin ')
        claveadmin=cur.fetchall()
        if request.method == 'POST':
            Username=request.form['username']
            Clave=request.form['password']
            i= len(usersadmin)
            global c
            while(c<i):
                if(usersadmin[c][0]==Username and  claveadmin[c][0]==Clave):
                    return idadmin[c][0]
                else:
                    c+=1              
    def convertir_float(self):
            global dataframe
            dataframe = pd.DataFrame(datos)
            data=['fixed acidity',
                    'volatile acidity',
                    'citric acid',
                    'residual sugar',
                    'chlorides',
                    'free sulfur dioxide',
                    'total sulfur dioxide',
                    'density','pH','sulphates','alcohol']   
            for c in range(0,len(data)):
                    for i in dataframe[data[c]]:
                        if i.__contains__(','):
                            new_value = i.replace(",", ".")
                            dataframe = dataframe.replace({ data[c]: { i: new_value }})
                    dataframe[data[c]] = dataframe[data[c]].astype(float)
                    print('Convirtiendo datos del CSV a float:',data[c])     
            return "Realizado"                     
    def m_predecir(self,fixedacidity,volatileacidity,
                                      citricacid,residualsugar,
                                      chlorides,freesulfurdioxide,
                                      totalsulfurdioxide,density,
                                      pH,sulphates,alcohol):
        self.convertir_float()
        X = (dataframe[["fixed acidity",
                        "volatile acidity",
                        "citric acid",
                        "residual sugar",
                        "chlorides",
                        "free sulfur dioxide",
                        "total sulfur dioxide",
                        "density","pH","sulphates","alcohol"]])
        y = (dataframe["quality"])

        #Entrenamiento
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.30,random_state=0)
        model = LogisticRegression( max_iter=10000)
        model.fit(X_train,y_train)
        datanew = {
                'fixed acidity':[fixedacidity],
                'volatile acidity':[volatileacidity],
                'citric acid':[citricacid],
                'residual sugar':[residualsugar],
                'chlorides':[chlorides],
                'free sulfur dioxide':[freesulfurdioxide],
                'total sulfur dioxide':[totalsulfurdioxide],
                'density':[density],
                'pH':[pH],
                'sulphates':[sulphates],
                'alcohol':[alcohol]}

        #nuevo cliente
        clientesnew = pd.DataFrame(datanew,columns=[
                'fixed acidity',
                'volatile acidity',
                'citric acid',
                'residual sugar',
                'chlorides',
                'free sulfur dioxide',
                'total sulfur dioxide','density','pH','sulphates','alcohol'])
        prediccion = model.predict(clientesnew)
        puntaje=model.score(X_test,y_test)
        print ("-Score-",puntaje)

        return prediccion
    
    def m_mensaje_flash(self,prediccion):
        if prediccion == 3:
            flash("3")
        elif prediccion == 4:
            flash("4")
        elif prediccion == 5:
            flash("5")
        elif prediccion == 6:
            flash("6")
        elif prediccion == 7:
            flash("7")
        elif prediccion == 8:
            flash("8")                                            

    def m_insertar_datos_pred(self,fixedacidity,volatileacidity,
                                      citricacid,residualsugar,
                                      chlorides,freesulfurdioxide,
                                      totalsulfurdioxide,density,
                                      pH,sulphates,alcohol,prediccion):
        prediccion_int=self.m_convertir_prediccion_int(prediccion)
        cur.execute("""
        INSERT INTO twine_prediction_user 
        (fixedacidity,volatileacidity,citricacid,
        residualsugar,chlorides,freesulfurdioxide,
        totalsulfurdioxide,density,
        ph,sulphates,alcohol,prediction)
        VALUES(%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s)""",
        (fixedacidity,volatileacidity,citricacid,
        residualsugar,chlorides,freesulfurdioxide,
        totalsulfurdioxide,density,
        pH,sulphates,alcohol,prediccion_int))        
        cnx.commit()

    def m_convertir_prediccion_int(self,prediccion):
        if prediccion == 3:
            prediccion_int= 3
        elif prediccion == 4:
            prediccion_int= 4
        elif prediccion == 5:
            prediccion_int= 5
        elif prediccion == 6:
            prediccion_int= 6
        elif prediccion == 7:
            prediccion_int= 7
        elif prediccion == 8:
            prediccion_int= 8
        return prediccion_int
    
    def m_actualizar_datos_prediccion(self,fixedacidity,volatileacidity,
                                                  citricacid,residualsugar,
                                                  chlorides,freesulfurdioxide,
                                                  totalsulfurdioxide,density,
                                                  pH,sulphates,alcohol,
                                                  prediction,id):
        sql = """
        UPDATE twine_prediction_user SET 
        fixedacidity=%s, volatileacidity=%s, citricacid=%s, 
        residualsugar=%s, chlorides=%s, freesulfurdioxide=%s, 
        totalsulfurdioxide=%s, density=%s, ph=%s, 
        sulphates=%s, alcohol=%s, prediction=%s 
        WHERE id = %s"""
        data = (fixedacidity,volatileacidity,
                citricacid,residualsugar,
                chlorides,freesulfurdioxide,
                totalsulfurdioxide,density,
                pH,sulphates,alcohol,
                prediction,id)
        cur.execute(sql,data)
        cnx.commit()
        #Datos Actualizados
        flash("1")        


    def m_verificar_token_expiro(self,tokenp,llave):
        try:
            tokenv = jwt.decode(tokenp,llave,algorithms="HS256")
            # si es 0 es valido
            tokenv = 0
        except:
            # si es 1 expiro o no es valido
            tokenv= 1
        return tokenv
    def m_delete_pred_user(self,id):
        sql = "DELETE FROM twine_prediction_user WHERE id=%s"
        data = (id,)
        cur.execute(sql,data)
        cnx.commit()