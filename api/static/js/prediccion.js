// Flecha de arriba
const btn_scrolltop = document.querySelector(".btn-Arrow_up")
// Flecha de abajo 
const divArrowDown = document.querySelector('.div-Arrow_down_pag_pred')
const IconoArrowDown = document.querySelector('.Arrow_down_pag_pred')
// Seccion a donde queremos ir
const finpag =document.querySelector(".footer-pag")


window.addEventListener('click', (e) => {
    //  console.log(e.target);
    // Deslizar hacia el fin de la pagina
    if (e.target == IconoArrowDown || e.target == divArrowDown){
        finpag.scrollIntoView(true);
    }
})


btn_scrolltop.addEventListener('click',()=>{
    window.scrollTo(0,0);
})

// Escucha cada vez que el scroll se mueve
window.onscroll =()=>{
    add_Btn_Scrolltop();
}

// Agregar boton de scroll hacia arriba
const add_Btn_Scrolltop = () =>{
    // console.log(window.scrollY)
    // Aparecer o desaparecer clase para que se borre la flecha hacia arriba
    if (window.scrollY > 200){
        btn_scrolltop.classList.add("btn-scrollArrow_up-on")
    }else{
        btn_scrolltop.classList.remove("btn-scrollArrow_up-on")
    }
    
}