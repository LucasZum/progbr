var idade = 19;

/*
if (idade >= 18){
    console.log("pode");
    console.log("Qual o seu pedido ?");
}

else{
    console.log("Não pode");
    console.log("Volte futuramente");
}
*/

//  OU //
//  "?" = if
//  ":" = else

var pode = idade <= 18 ? true : false;

if (pode == true){
    console.log("não pode");
    console.log("Volte futuramente");
}
else{
    console.log("PODEEE");
}