
const firebaseConfig = {

    apiKey: "AIzaSyBxfiuXuhpBik8-zPG6gqEHash97C6ZIXg",
  
    authDomain: "meusite-14797.firebaseapp.com",
  
    projectId: "meusite-14797",
  
    storageBucket: "meusite-14797.appspot.com",
  
    messagingSenderId: "55226634612",
  
    appId: "1:55226634612:web:f32ebfd41b47c8dc565c21",
  
    measurementId: "G-XTWVJ258ZE"
  
  };



    firebase.initializeApp(firebaseConfig)
    let db = firebase.firestore()

    let meudb = "MeuSitedb"
    let nomea = document.getElementById("nome")
    let sobrenomea = document.getElementById("sobrenome")
    let emaila = document.getElementById("email")
    let button = document.getElementById("button")
    
    
    button.addEventListener("click", enviar);
    
    function enviar() {
    
        let nomev = nomea.value 
        let sobrenomev = sobrenomea.value 
        let emailv = emaila.value
    
        db.collection(meudb).add({
            nome: nomev,
            email: emailv,
        }).then((doc)=>{
            console.log("documento enserido com sucesso");
        })
    }
