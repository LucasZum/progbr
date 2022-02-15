  // Import the functions you need from the SDKs you need

  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.6/firebase-app.js";

  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.6.6/firebase-analytics.js";

  // TODO: Add SDKs for Firebase products that you want to use

  // https://firebase.google.com/docs/web/setup#available-libraries


  // Your web app's Firebase configuration

  // For Firebase JS SDK v7.20.0 and later, measurementId is optional

  const firebaseConfig = {

    apiKey: "AIzaSyBxfiuXuhpBik8-zPG6gqEHash97C6ZIXg",

    authDomain: "meusite-14797.firebaseapp.com",

    projectId: "meusite-14797",

    storageBucket: "meusite-14797.appspot.com",

    messagingSenderId: "55226634612",

    appId: "1:55226634612:web:36f03ac8189cb007565c21",

    measurementId: "G-R4KEFPP7VW"

  };


  // Initialize Firebase

  const app = initializeApp(firebaseConfig);

  const analytics = getAnalytics(app);
