

function aumentarLetra(){
var font = document.getElementById("Conteudo").style.fontSize;
font = font.replace("px","");

if(font == ""){
document.getElementById("Conteudo").style.fontSize = "100%";
}else{
    if (font === "150%"){   }
    else {
        document.getElementById("Conteudo").style.fontSize = (parseInt(font)+10)+"%";
    }
}
}

function diminuirLetra(){
var font = document.getElementById("Conteudo").style.fontSize;
font = font.replace("px","");
if(font == ""){
document.getElementById("Conteudo").style.fontSize = "100%";
}else{
       if (font === "80%") {
       }
       else{
        document.getElementById("Conteudo").style.fontSize = (parseInt(font)-10)+"%";
        }

}
}