



function criarAluno(nome, n1, n2){
    return{
        nome:nome,
        nota1: n1,
        nota2: n2,
        media:function(){
            return(this.nota1 + this.nota2)/2
        }
    }
}

var turma = [
    criarAluno("Lucas", 10, 8)
]
var aluno = turma[0]

console.log(aluno);
console.log(aluno.media());