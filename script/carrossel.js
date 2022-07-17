const imgs = document.getElementById('imgs')
const img = document.querySelectorAll('#imgs img')

let id = 0

function carrossel() {
    id ++

    if(id > img.length - 1){
        id = 0
    }

    imgs.style.transform = `translatex(${-id * 100}vw)`
}

setInterval(carrossel, 1800)