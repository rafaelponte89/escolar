
// a criação de cookies possibilita armazenar configurações do site no navegador
function configuracoes(){
    document.getElementById("Conteudo").style.fontSize = pegarCookie("tamanhoLetra") + "%";
    }


function criarCookie(nome,valor){
    document.cookie = nome + "=" + valor;
}

// https://www.w3schools.com/js/js_cookies.asp
// https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie
function pegarCookie(nome) {

    if (!document.cookie.split('; ').find(row => row.startsWith(nome)))
    {
          criarCookie("tamanhoLetra","100");
    }

   const cookieValue = document.cookie
  .split('; ')
  .find(row => row.startsWith(nome))
  .split('=')[1];

   return cookieValue;
}

function processarTamanhoLetra(limiteFonte, operacao)
{
     let font = pegarCookie("tamanhoLetra");

        if (font === limiteFonte){}
        else {

            if (operacao == "+"){
                font = (parseInt(font) + 10);
            }
            else {
                font = (parseInt(font) - 10);
            }
            document.getElementById("Conteudo").style.fontSize =  font + "%";
        }

        criarCookie("tamanhoLetra",font);

}

function aumentarLetra(){
    processarTamanhoLetra("150","+")
}

function diminuirLetra(){
    processarTamanhoLetra("80","-")
}

