

let inputAdultos = document.getElementById("adultos")
let inputCriancas = document.getElementById("criancas")
let inputDuracao = document.getElementById("duracao")
let resultado = document.getElementById("resultado")

function calcular(){

    let adultos = inputAdultos.value 
    let criancas = inputCriancas.value
    let duracao = inputDuracao.value

    let carne = carnePP(duracao) * adultos + (carnePP(duracao) / 2 * criancas)
    let cerveja = cervejaPP(duracao) * adultos
    let bebidas = bebidaPP(duracao) * adultos + (bebidaPP(duracao) / 2 * criancas)

    resultado.innerHTML = `<p>${carne / 1000}kg de Carne</p>`
    resultado.innerHTML += `<p>${Math.ceil(cerveja/355)}Latas de Cerveja de 355ml</p>`
    resultado.innerHTML += `<p>${Math.ceil(bebidas/2000)}Garrafas de 2L de Bebidas</p>`

}
function carnePP(duracao){
    if (duracao >= 6){
        return 650;
    }else{
        return 450;
    }
}
function cervejaPP(duracao){
    if (duracao >= 6){
        return 2000;
    }else{
        return 1200;
    }
}
function bebidaPP(duracao){
    if (duracao >= 6){
        return 1500;
    }else{
        return 1000;
    }
}