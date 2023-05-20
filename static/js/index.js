// Buton para modal
const btnIndex = document.querySelector('.index-btn');
const modal = document.querySelector('.modal-teamdev');
const modalC = document.querySelector('.modal-container');
// Flecha de abajo en imagen del header
const divArrowDown = document.querySelector('.div-Arrow_down')
const IconoArrowDown = document.querySelector('.Arrow_down')
const primerTituloIndex =document.querySelector(".index-subtitle")
// Flecha de arriba
const btn_scrolltop = document.querySelector(".btn-Arrow_up")


//Boton del modal
btnIndex.addEventListener('click', () => {
    modalC.style.opacity = "1";
    modalC.style.visibility = "visible";
    modal.classList.remove("modal-close");
    //Remover boton de scroll hacia arriba
    btn_scrolltop.classList.remove("btn-scrollArrow_up-on")
})

btn_scrolltop.addEventListener('click',()=>{
    window.scrollTo(0,0);
})

window.addEventListener('click', (e) => {
    //  console.log(e.target);
    //Abrir modal
    if(e.target == modalC){
        modal.classList.add("modal-close");
        //Agregar boton de scroll hacia arriba
        btn_scrolltop.classList.add("btn-scrollArrow_up-on")
        setTimeout( () =>{
        modalC.style.opacity = "0";
        modalC.style.visibility = "hidden";
        },900)
    }
    // Deslizar hacia el primer titulo del index
    if (e.target == IconoArrowDown || e.target == divArrowDown){
        primerTituloIndex.scrollIntoView(true);
    }
})

// Escucha cada vez que el scroll se mueve
window.onscroll =()=>{
    add_Btn_Scrolltop();
}

// Agregar boton de scroll hacia arriba
const add_Btn_Scrolltop = () =>{
        // Aparecer o desaparecer clase para que se borre la flecha hacia arriba
        if (window.scrollY > 700){
            btn_scrolltop.classList.add("btn-scrollArrow_up-on")
        }else{
            btn_scrolltop.classList.remove("btn-scrollArrow_up-on")
        }
        //console.log(window.scrollY)
}