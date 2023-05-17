// Buton para modal
const btnIndex = document.querySelector('.index-btn');

const modal = document.querySelector('.modal');
const modalC = document.querySelector('.modal-container');

btnIndex.addEventListener('click', () => {
    modalC.style.opacity = "1";
    modalC.style.visibility = "visible";
    modal.classList.remove("modal-close");
})

window.addEventListener('click', async (e) => {
    // console.log(e.target);
    if(e.target == modalC){
        modal.classList.add("modal-close");
        setTimeout( () =>{
        modalC.style.opacity = "0";
        modalC.style.visibility = "hidden";
        },900)
    }
})