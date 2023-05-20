
const divToken= document.getElementById("token");
var token = divToken.textContent;

const enlaceLogin = document.getElementById("nodo-login");

// Si tiene un token valido quiere decir que se logeo bien
// Quitar iniciar session y poner los enlaces de admin y cerrar session
try{
    decode=JSON.parse (atob(token.split('.')[1]));
    mensaje= "base-token valido";
    console.log(mensaje);
    //Cuando esta logeado osea tiene token se remueve enlace login
    enlaceLogin.remove();
    // Se agrega los enlaces de admin y cerrar session(logout) 
    agregarElementsEnlaceAdmin();
}catch (e){
    mensaje= "Token no es valido o ya expiro";
    console.log(mensaje);
}
console.log("Token:",token);

function agregarElementsEnlaceAdmin() {
    // Crear un nuevo elemento <li>
    //<li><a href="contact_Us_Admin">Contáctenos Admin </a></li>
    let li_contact_us_admin = document.createElement("li");
    let li_prediccion_admin =document.createElement("li");
    let li_logout = document.createElement("li");
  
    // Crear  elementos <a> dentro del <li>
    let enlace_prediccion_admin = document.createElement("a");
    enlace_prediccion_admin.href="prediccion_Admin";
    enlace_prediccion_admin.textContent = "Prediccion-Admin";

    let enlace_contact_us_admin = document.createElement("a");
    enlace_contact_us_admin.href="contact_Us_Admin";
    enlace_contact_us_admin.textContent = "Contáctenos-Admin";

    let enlacelogout = document.createElement("a");
    enlacelogout.href = "logout"; // URL de cierre de sesión
    enlacelogout.textContent = "Cerrar sesión"; // Texto del enlace
    
    // Agregar el elemento <a> al elemento <li>
    li_contact_us_admin.appendChild(enlace_contact_us_admin);
    li_prediccion_admin.appendChild(enlace_prediccion_admin)
    li_logout.appendChild(enlacelogout);
    
    // Obtener el contenedor por su ID
    var contenedor = document.getElementById("lists");
  
    // Insertar el nuevo elemento <li> como último hijo del contenedor
    contenedor.appendChild(li_contact_us_admin);
    contenedor.appendChild(li_prediccion_admin);
    contenedor.appendChild(li_logout);
  }