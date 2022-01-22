

var alunos = ["lucas", "leticia", "isa"]
var notasA = [10, 7, 2]
var notasB = [7, 8 ,5]

function media(n1, n2){
    return (n1 + n2)/2
}
function passou(media){

    if(media >= 7){
        return "aprovado"
    }else{
        return "Reprovado"
    }
}

for (var i in alunos){

    var nota1 = notasA[i]
    var nota2 = notasB[i]
    var m = media(nota1, nota2)

    console.log(alunos[i] + " - " + nota1 + " - " + nota2 + " - " + m + " - " + passou(m));

}