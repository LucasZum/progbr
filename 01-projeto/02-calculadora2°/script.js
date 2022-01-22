

let elementa = document.getElementById("a")
let elementb = document.getElementById("b")
let elementc = document.getElementById("c")
let res = document.getElementById("res")

function calcular(){


    let a = elementa.value
    let b = elementb.value
    let c = elementc.value
    
    let delta = b**2 -4*a*c
    if(delta >= 0){
        let rdelta = Math.sqrt(delta)
        let x1 = (-b - rdelta)/(2*a)
        let x2 = (-b + rdelta)/(2*a)
        if(delta == 0){
            res.innerHTML = `<p>Só possui uma Raiz: ${x1}</p>`
        }else{
            res.innerHTML = `<p>As raizes dessa equação são:<br><br><br>X1 = ${x1}<br>X2 = ${x2}</p>`
        }
    }else{
        res.innerHTML = `<p>Não possui Raizes reais`
    }
}
