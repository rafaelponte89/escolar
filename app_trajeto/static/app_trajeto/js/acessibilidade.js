
// a criação de cookies possibilita armazenar configurações do site no navegador
function configuracoes(){
    document.getElementById("Conteudo").style.fontSize = getCookie("tamanhoLetra") + "%"
}

function criarCookie(nome,valor){
    document.cookie = nome + "=" + valor;
}


// https://www.w3schools.com/js/js_cookies.asp
function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}


function aumentarLetra(){

    let font = getCookie("tamanhoLetra");

        if (font === "150"){}
        else {

            if (font == ""){
                font = 100;
            }
            font = (parseInt(font)+10);
            document.getElementById("Conteudo").style.fontSize =  font + "%";

        }
        criarCookie("tamanhoLetra",font);


}

function diminuirLetra(){

    let font = getCookie("tamanhoLetra");

        if (font === "80"){

        }
        else {

            if (font == ""){
                font = 100;
            }
            font = (parseInt(font)-10);
            document.getElementById("Conteudo").style.fontSize =  font + "%";

        }
        criarCookie("tamanhoLetra",font);
}