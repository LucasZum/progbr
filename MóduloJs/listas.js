

let lista = document.getElementById("lista")
let num = parseInt(lista)

let conteudo = ""
i = 1
while(i < num + 1){
    conteudo += "<li>" + i + "</li>"
    i++
}
lista.innerHTML = conteudo