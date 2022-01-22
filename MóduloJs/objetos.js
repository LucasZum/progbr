

function calcMedia(n1,n2){
    return (this.notas[0] + this.notas[1]) / 2;
}
var aluno = {
    nome:"Lucas",
    notas: [10, 9],

    media = calcMedia
}
var aluno1 = {
    nome:"carlos",
    notas: [6, 9],

    media = calcMedia
}
console.log(aluno.nome);
console.log(media(aluno.notas[0], aluno.notas[1]));

console.log(aluno1.nome);
console.log(media(aluno1.notas[0], aluno1.notas[1]));