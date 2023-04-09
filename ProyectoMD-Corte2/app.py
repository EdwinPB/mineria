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
#------------------------------------------- Pagina dashboard--------------------------------------------
@app.route('/dashboard.html')
def Pagdashboard():
    cur.execute('SELECT * FROM templeodev')
    result=cur.fetchall()
    #Convertir los datos a diccionario
    insertObject= []
    columnNames = [column[0] for column in cur.description]
    for record in result:
        insertObject.append(dict(zip(columnNames,record)))
    return render_template('dashboard.html',data=insertObject)   

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
        return render_template('login.html')

#------------------------------------------- Pagina gestion de datos-------------------------------------
@app.route('/gestiondatos.html')
## obtener data y mandar a un html
def pagGestionDatos():
    cur.execute('SELECT * FROM templeodev')
    result=cur.fetchall()
    #Convertir los datos a diccionario
    insertObject= []
    columnNames = [column[0] for column in cur.description]
    for record in result:
        insertObject.append(dict(zip(columnNames,record)))
    
    return render_template('gestiondatos.html',data=insertObject)
@app.route('/add', methods=['POST'])
def add():
    nombre= request.form["nombre"]
    ciudad= request.form["ciudad"]
    salario= request.form["salario"]
    fechav= request.form["fechav"]
    yearExp= request.form["yearExp"]
    numVacantes= request.form["numVacantes"]    

    if len(nombre and ciudad and salario and fechav and yearExp and numVacantes) >= 1:
        cur.execute("""INSERT INTO templeodev (Nombre,Ciudad,Salario
        ,FechaPublicacion,FechaVencimiento,YearExp,NumeroVacantes)
        VALUES(%s,%s,%s,CURDATE(),%s,%s,%s)""",
        (nombre,ciudad,salario,fechav,yearExp,numVacantes))        
        cnx.commit()
        # MENSAJE (datos insertados)
        flash("2")
    else:
        # MENSAJE (llenar todos los campos)
        flash("1")
    return redirect(url_for('pagGestionDatos'))


@app.route('/delete/<id>')
def delete(id):
    sql = "DELETE FROM templeodev WHERE IdEmpleo=%s"
    data = (id,)
    cur.execute(sql,data)
    cnx.commit()
    #Dato Eliminado
    flash('0')
    return redirect(url_for('pagGestionDatos'))


@app.route('/edit/<id>', methods=['POST'])
def edit(id):
    nombre= request.form["nombre"]
    ciudad= request.form["ciudad"]
    salario= request.form["salario"]
    fechav= request.form["fechav"]
    yearExp= request.form["yearExp"]
    numVacantes= request.form["numVacantes"]       
    sql = """UPDATE templeodev SET Nombre=%s, Ciudad=%s, Salario=%s, 
    FechaPublicacion=CURDATE(), FechaVencimiento=%s, YearExp=%s, NumeroVacantes=%s 
    WHERE IdEmpleo = %s"""
    data = (nombre,ciudad,salario,fechav,yearExp,numVacantes,id)
    cur.execute(sql,data)
    cnx.commit()
    #Dato Editado
    flash('3')
    return redirect(url_for('pagGestionDatos'))
     
#--------------------------------------------------------------------------------------------------------


#------------Redirijir a cliente a login cuando ingrese a una pagina que no este definida---------------
def pagina_no_encontrada(error):
     return redirect(url_for('Paglogin'))
#-----------------------------------------------MAIN-----------------------------------------------------
if __name__== '__main__':
    app.register_error_handler(404,pagina_no_encontrada)
    app.run(debug=True)