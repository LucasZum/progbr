var n1 = 10.0;
var n2 = 10.0;

var media = (n1 + n2) / 2;

if (media >= 8){
    conceito = "Ótimo";
}
else if (media >= 6){
    conceito = "Bom";
}
else{
    conceito = "Regular";
}

switch(conceito){

    case("Ótimo"):
        console.log(conceito + ": " + media);
        console.log("Voce é um aluno perfeito");
        break
    
    case("Bom"):
        console.log(conceito + ": " + media);
        console.log("voce é um aluno quase prefeito");
        break
    
    case("Regular"):
        console.log(conceito + ": " + media);
        console.log("Estude mais");
        break
    
    default:
        console.log("Bugo");
        break







}