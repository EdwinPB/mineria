# 1-Le pide la informacion al modelo para un usuario que no esta autenticado
# 3- la envia a la vista
# aqui va hacia donde quieres que se dirija el usuario y se lo pasa
# al controlador
from model.model import *
modelo= model()
class controller():
    def c_verificar_usuario(self):
        query= modelo.m_verificar_admin_usuario()
        return query
    def c_crear_token_usuario(self):
        token = modelo.m_crear_token_admin_usuario()
        return token
    def c_predecir(self,fixedacidity,volatileacidity,
                                      citricacid,residualsugar,
                                      chlorides,freesulfurdioxide,
                                      totalsulfurdioxide,density,
                                      pH,sulphates,alcohol):
        prediccion= modelo.m_predecir(fixedacidity,volatileacidity,
                                      citricacid,residualsugar,
                                      chlorides,freesulfurdioxide,
                                      totalsulfurdioxide,density,
                                      pH,sulphates,alcohol)
        modelo.m_insertar_datos_pred(fixedacidity,volatileacidity,
                                      citricacid,residualsugar,
                                      chlorides,freesulfurdioxide,
                                      totalsulfurdioxide,density,
                                      pH,sulphates,alcohol,prediccion[0])
        return prediccion
    
    def c_mensaje_flash(self,prediccion):
        modelo.m_mensaje_flash(prediccion)
    
        
    def c_verificar_token_expiro(self,tokenp,llave):
        query= modelo.m_verificar_token_expiro(tokenp,llave)
        return query
    
    ## Pagina Predicion admin (Crud)
    
    def c_listar_twine_pag_pred(self):
        query=modelo.m_listar_twine_pag_pred()
        return query

    def c_actualizar_datos_prediccion(self,fixedacidity,volatileacidity,
                                                  citricacid,residualsugar,
                                                  chlorides,freesulfurdioxide,
                                                  totalsulfurdioxide,density,
                                                  pH,sulphates,alcohol,prediction,id):
        modelo.m_actualizar_datos_prediccion(fixedacidity,volatileacidity,
                                                  citricacid,residualsugar,
                                                  chlorides,freesulfurdioxide,
                                                  totalsulfurdioxide,density,
                                                  pH,sulphates,alcohol,prediction,id)

    def c_delete_pred_user(self,id):
        modelo.m_delete_pred_user(id)

    ## Pagina Contact us admin (Crud)   
    def c_listar_tcontact_us_pag_contactus_admin(self):
        query=modelo.m_listar_tcontact_us_pag_contactus_admin()
        return query

    def c_editar_pag_contact_us_admin(self,nombre,correo,mensaje,id):
        modelo.m_editar_pag_contact_us_admin(nombre,correo,mensaje,id)

    def c_delete_pag_contact_us_admin(self,id):
        modelo.m_delete_pag_contact_us_admin(id)


    # Pagina Contact us
    def c_add_registro_pag_contact_us(self,nombre,correo,mensaje):
        modelo.m_add_registro_pag_contact_us(nombre,correo,mensaje)