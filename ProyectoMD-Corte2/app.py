from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import *
#Importar modulo conexion
from conexion import *

app= Flask(__name__)

#-----------------------------Settings (Como va ir protegida la session)--------------------------------
app.secret_key= 'mysecretkey'
#-------------------------------------------Sitio web de la pagina principal----------------------------
#-------------------------------------------- Pagina login ---------------------------------------------
@app.route('/login.html')
def Paglogin():
    return render_template('login.html')
#------------------------------------------- Pagina Principal-------------------------------------------
@app.route('/index.html')
def Index():
    return render_template('index.html')   

#--------------------------------------------------------------------------------------------------------
#------------------------------------------- Pagina gestion de datos-------------------------------------
@app.route('/gestiondatos.html')
def Paggestiondatos():
    return render_template('gestiondatos.html')   

#--------------------------------------------------------------------------------------------------------
#------------------------------------------- Pagina dashboard--------------------------------------------
@app.route('/dashboard.html')
def Pagdashboard():
    return render_template('dashboard.html')   

#--------------------------------------------------------------------------------------------------------
#------------------------------------------- Pagina Acerca de-------------------------------------
@app.route('/acercade.html')
def Pagacercade():
    return render_template('acercade.html')   

#--------------------------------------------------------------------------------------------------------
#---------------------------------------------   route login---------------------------------------------
@app.route('/login', methods=["GET","POST"])
def login():
    cur.execute('SELECT NombreUsuario FROM tusuarios')
    users=cur.fetchall()
    cur.execute('SELECT Clave FROM tusuarios')
    clave=cur.fetchall()        
    if request.method == 'POST':
        #Boton que se presiono
        btn=request.form['btn']
        #Input
        Username=request.form['username']
        Clave=request.form['password']
        global c
               
        #Boton Login
        if btn == "1":
            c=0
            i=len(users)
            while(c<i):
                if(users[c][0]==Username and  clave[c][0]==Clave):
                    return redirect(url_for('Index'))
                else:
                    c+=1              
            #0=invalid username or password
            flash('0')
            return redirect(url_for('Paglogin'))
        
        #Boton Check In
        elif btn == "2":                    
            if len(Username and Clave) >= 1:
                cur.execute('INSERT INTO tusuarios (NombreUsuario,Clave) VALUES(%s,%s)',(Username,Clave))
                cnx.commit()             
                #(1) successfully registered user 
                flash('1')
            else:
                #(2)Unregistered user
                flash('2')                    
    
            return redirect(url_for('Paglogin'))
        
    else:    
        return render_template('login,html')


#------------Redirijir a cliente a login cuando ingrese a una pagina que no este definida---------------
def pagina_no_encontrada(error):
     return redirect(url_for('Paglogin'))
#-----------------------------------------------MAIN-----------------------------------------------------
if __name__== '__main__':
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True)