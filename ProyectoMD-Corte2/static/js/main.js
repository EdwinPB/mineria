//Login 
//Texto Username (Que no coloque espacios)
_textoUInput.addEventListener("keyup",e=>{
    let string = e.target.value
    e.target.value = string.split(" ").join("");
})
//Texto Password (Que no coloque espacios)
_textoPInput.addEventListener("keyup",e=>{
    let string = e.target.value
    e.target.value = string.split(" ").join("");
})
