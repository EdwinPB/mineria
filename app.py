# pip install flask
from flask import Flask, render_template,request,redirect,url_for,flash,session
from config import *
from controller.controller import *
from functools import wraps

# Controller
controlador= controller()


appf= Flask(__name__)

#-----------------------------Settings (Como va ir protegida la session)--------------------------------
appf.config['SECRET_KEY']= 'mysecretkey'


def token_required(f):
     @wraps(f)
     def decorator(*args, **kwargs):
          print ("Token Python Para proteger rutas--",session['token'])
          try:
               payload = jwt.decode(session['token'],appf.config['SECRET_KEY'],algorithms="HS256")
               print (payload)
          except Exception as e:
               print ("El token no es valido o ya expiro")
               #No puede acceder porque el token no es valido o ya expiro
               flash("3")
               return redirect(url_for('PagLogin'))
          return f(*args, **kwargs)
     return decorator

#------------------Rutas de usuario
@appf.route('/login', methods=["GET","POST"])
def PagLogin():
     if request.method == 'POST':
          resp=controlador.c_verificar_usuario()
          
          # Si el usuario existe la respuesta dara logeado
          if resp == "logeado":
               session['token'] = controlador.c_crear_token_usuario()
               return redirect(url_for('index'))
          ##invalid username or password        
          flash("0")
          return redirect(url_for('PagLogin'))
     else:
          if session['token'] == None:
               session['token']=0
               tokenp=session['token']
          else:
               tokenp=session['token']
               #si el resultado es 0 es valido si es 1 ya expiro o no es valido
               tokenv=controlador.c_verificar_token_expiro(tokenp,appf.config['SECRET_KEY'])
               if tokenv == 0:
                    tokenp=session['token']
               else:
                    session['token']=0
                    tokenp=session['token']
          return render_template('login.html',token=tokenp)
     
@appf.route('/')
def index():
     try:
          if   ['token'] == None:
               session['token']=0
               tokenp=session['token']
          else:
               tokenp=session['token']
               #si el resultado es 0 es valido si es 1 ya expiro o no es valido
               tokenv=controlador.c_verificar_token_expiro(tokenp,appf.config['SECRET_KEY'])
               if tokenv == 0:
                    tokenp=session['token']
               else:
                    session['token']=0
                    tokenp=session['token']
     except Exception as e:
          session['token']=0
          tokenp=session['token']

     return render_template('index.html',token=tokenp) 

@appf.route('/about_Us')
def PagAboutUs():
     try:
          if session['token'] == None:
               session['token']=0
               tokenp=session['token']
          else:
               tokenp=session['token']
               #si el resultado es 0 es valido si es 1 ya expiro o no es valido
               tokenv=controlador.c_verificar_token_expiro(tokenp,appf.config['SECRET_KEY'])
               if tokenv == 0:
                    tokenp=session['token']
               else:
                    session['token']=0
                    tokenp=session['token']
     except Exception as e:
          session['token']=0
          tokenp=session['token']

     return render_template('about_Us.html',token=tokenp)

@appf.route('/prediccion')
def PagPrediccion():
     try:
          if session['token'] == None:
               session['token']=0
               tokenp=session['token']
          else:
               tokenp=session['token']
               #si el resultado es 0 es valido si es 1 ya expiro o no es valido
               tokenv=controlador.c_verificar_token_expiro(tokenp,appf.config['SECRET_KEY'])
               if tokenv == 0:
                    tokenp=session['token']
               else:
                    session['token']=0
                    tokenp=session['token']
     except Exception as e:
          session['token']=0
          tokenp=session['token']
     return render_template('prediccion.html',token=tokenp)


@appf.route('/prediccion/add', methods=["POST"])
def Prediccion():
     fixedacidity=request.form["fixedacidity"]
     volatileacidity=request.form["volatileacidity"]
     citricacid=request.form["citricacid"]
     residualsugar=request.form["residualsugar"]
     chlorides=request.form["chlorides"]
     freesulfurdioxide=request.form["freesulfurdioxide"]
     totalsulfurdioxide=request.form["totalsulfurdioxide"]
     density=request.form["density"]
     pH=request.form["pH"]
     sulphates=request.form["sulphates"]
     alcohol=request.form["alcohol"]
     
     if len(fixedacidity and volatileacidity and citricacid
               and residualsugar and chlorides and freesulfurdioxide
               and totalsulfurdioxide and density
               and pH and sulphates and alcohol) >= 1:
          prediccion=controlador.c_predecir(fixedacidity,volatileacidity,
                                                  citricacid,residualsugar,
                                                  chlorides,freesulfurdioxide,
                                                  totalsulfurdioxide,density,
                                                  pH,sulphates,alcohol
                                                  ) 
          # Prediccion
          controlador.c_mensaje_flash(prediccion[0])
          
          
     else:
          #Complete todos los datos
          flash("0")
     return redirect(url_for('PagPrediccion'))

@appf.route('/contact_Us')
def PagContactUs():
     try:
          if session['token'] == None:
               session['token']=0
               tokenp=session['token']
          else:
               tokenp=session['token']
               #si el resultado es 0 es valido si es 1 ya expiro o no es valido
               tokenv=controlador.c_verificar_token_expiro(tokenp,appf.config['SECRET_KEY'])
               if tokenv == 0:
                    tokenp=session['token']
               else:
                    session['token']=0
                    tokenp=session['token']
     except Exception as e:
          session['token']=0
          tokenp=session['token']
     return render_template('contact_Us.html',token=tokenp)

@appf.route('/contact_Us/add', methods=["POST"])
def add():
    nombre= request.form["name"]
    correo= request.form["email"]
    mensaje= request.form["message"]  
    if len(nombre and correo and mensaje) >= 1:
        controlador.c_add_registro_pag_contact_us(nombre,correo,mensaje)
        # MENSAJE (datos insertados)
        flash("0")
    else:
        # MENSAJE (llenar todos los campos)
        flash("1")
    return redirect(url_for('PagContactUs'))



#------Rutas admin
@appf.route('/contact_Us_Admin', methods=["GET","POST"])
@token_required
def PagContactUsAdmin():
     if request.method == 'GET':
          insertObject=controlador.c_listar_tcontact_us_pag_contactus_admin()
          return render_template('contact_us_admin.html',data=insertObject)

@appf.route('/delete/<id>')
@token_required
def delete(id):
     controlador.c_delete_pag_contact_us_admin(id)
     #dato eliminado
     flash("2")
     return redirect(url_for('PagContactUsAdmin'))

@appf.route('/edit/<id>', methods=['POST'])
@token_required
def edit(id):
     nombre= request.form["nombre"]
     correo= request.form["correo"]
     mensaje= request.form["mensaje"]
     controlador.c_editar_pag_contact_us_admin(nombre,correo,mensaje,id)
     #Datos Actualizado
     flash("1")
     return redirect(url_for('PagContactUsAdmin'))

@appf.route('/prediccion_Admin', methods=["GET","POST"])
@token_required
def PagPrediccionAdmin():
     if request.method == 'GET':
          insertObject=controlador.c_listar_twine_pag_pred()
          return render_template('prediccion_admin.html',data=insertObject)
     
@appf.route('/edit_prediccion_Admin/<id>', methods=['POST'])
@token_required
def edit_pred_admin(id):
     fixedacidity=request.form["fixedacidity"]
     volatileacidity=request.form["volatileacidity"]
     citricacid=request.form["citricacid"]
     residualsugar=request.form["residualsugar"]
     chlorides=request.form["chlorides"]
     freesulfurdioxide=request.form["freesulfurdioxide"]
     totalsulfurdioxide=request.form["totalsulfurdioxide"]
     density=request.form["density"]
     pH=request.form["ph"]
     sulphates=request.form["sulphates"]
     alcohol=request.form["alcohol"]
     prediction=request.form["prediction"]
     controlador.c_actualizar_datos_prediccion(fixedacidity,volatileacidity,
                                                  citricacid,residualsugar,
                                                  chlorides,freesulfurdioxide,
                                                  totalsulfurdioxide,density,
                                                  pH,sulphates,alcohol,prediction,id)
     return redirect(url_for('PagPrediccionAdmin')) 
@appf.route('/delete_pred_user/<id>')
@token_required
def delete_pred_user(id):
    controlador.c_delete_pred_user(id)
    #dato eliminado
    flash("2")

    return redirect(url_for('PagPrediccionAdmin'))

@appf.route('/logout')
def logout():
     session['token']=0
     #Se cerro session el token fue eliminado
     flash("2")
     return redirect(url_for('PagLogin'))

#------------Redirijir a cliente a login cuando ingrese a una pagina que no este definida---------------
def pagina_no_encontrada(error):
     return "<h1>La pagina a la que intentas acceder no existe...</h1>"

#-----------------------------------------------MAIN-----------------------------------------------------
if __name__== '__main__':
     appf.register_error_handler(404,pagina_no_encontrada)
     appf.run(debug=True)