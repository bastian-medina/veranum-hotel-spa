document.getElementById("btnIniciarSesion").addEventListener("click", login);
document.getElementById("btnRegister").addEventListener("click", register);
window.addEventListener("resize", anchoPagina)


var ContenedorLoginRegister = document.querySelector(".contenedorLoginRegister");
var formularioLogin = document.querySelector(".formularioLogin");
var formularioRegister = document.querySelector(".formularioRegister");
var cajaTraseraLogin = document.querySelector(".cajaLogin");
var cajaTraseraRegister = document.querySelector(".cajaRegister");


function anchoPagina(){
    if(window.innerWidth > 850){
        cajaTraseraLogin.style.display = "block";
        cajaTraseraRegister.style.display = "block";
    }else{
        cajaTraseraRegister.style.display = "block";
        cajaTraseraRegister.style.opacity = "1";
        cajaTraseraLogin.style.display = "none";
        formularioLogin.style.display = "block";
        formularioRegister.style.display= "none";
        ContenedorLoginRegister.style.left = "0px";
    }
}

anchoPagina();

function login(){
    if(window.innerWidth > 850){
        formularioRegister.style.display = "none";
        ContenedorLoginRegister.style.left = "10px";
        formularioLogin.style.display = "block";
        cajaTraseraRegister.style.opacity = "1";
        cajaTraseraLogin.style.opacity = "0";
    }else{
        formularioRegister.style.display = "none";
        ContenedorLoginRegister.style.left = "0px";
        formularioLogin.style.display = "block";
        cajaTraseraRegister.style.display = "block";
        cajaTraseraLogin.style.display = "none";
    } 
}

function register(){
    if(window.innerWidth > 850){
        formularioRegister.style.display = "block";
        ContenedorLoginRegister.style.left = "410px";
        formularioLogin.style.display = "none";
        cajaTraseraRegister.style.opacity = "0";
        cajaTraseraLogin.style.opacity = "1";
    }else{
        formularioRegister.style.display = "block";
        ContenedorLoginRegister.style.left = "0px";
        formularioLogin.style.display = "none";
        cajaTraseraRegister.style.display = "none";
        cajaTraseraLogin.style.display = "block";
        cajaTraseraLogin.style.opacity = "1";
    }
    
}