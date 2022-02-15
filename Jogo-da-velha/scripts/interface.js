

document.addEventListener("DOMContentLoaded", ()=>{

    let squares = document.querySelectorAll(".square")

    squares.forEach((square)=>{
        square.addEventListener("click", handleClick)
    })

})
function handleClick(evento){

    let square = evento.target
    let position = square.id 

    if (handleMove(position)){
        setTimeout(()=>{
            res.innerHTML = `<p>O jogo Acabou - O vencedor foi o player ${playerTime + 1}`
        }, 10)
    }
    updateSquares()

}

function updateSquares(){

    let squares = document.querySelectorAll(".square")

    squares.forEach((square)=>{

        let position = square.id
        let symbol = board[position]

        if (symbol != ''){
            square.innerHTML = `<div class="${symbol}"></div>`
        }
    })

}