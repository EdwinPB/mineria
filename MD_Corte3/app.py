from flask import Flask, render_template,request,redirect,url_for,flash
# from flask_mysqldb import *
from config import *

#Importar modulo conexion
# from conexion import *

appf= Flask(__name__)

#-----------------------------Settings (Como va ir protegida la session)--------------------------------
appf.config['SECRET_KEY']= 'mysecretkey'

@appf.route('/')
def index():
     return render_template('index.html') 

@appf.route('/contact_Us.html')
def PagContactUs():
    return render_template('contact_Us.html')

@appf.route('/about_Us.html')
def PagAboutUs():
    return render_template('about_Us.html')

@appf.route('/login.html')
def PagLogin():
     return render_template('login.html')

#------------Redirijir a cliente a login cuando ingrese a una pagina que no este definida---------------
def pagina_no_encontrada(error):
     return "<h1>La pagina a la que intentas acceder no existe...</h1>"

#-----------------------------------------------MAIN-----------------------------------------------------
if __name__== '__main__':
     appf.register_error_handler(404,pagina_no_encontrada)
     appf.run(debug=True)