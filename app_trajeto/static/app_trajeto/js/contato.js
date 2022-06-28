
const elem = document.getElementById('mensagemSugestao');
const modalMensagem = M.Modal.init(elem, {dismissible:false});

var gravarSugestao = document.getElementById('gravarSugestao');




gravarSugestao.addEventListener('click', function(event){
    
    document.getElementById('formSugestao').submit();
   
    
});

modalMensagem.open();

setTimeout(esperar,5000)

function esperar(){
    modalMensagem.close();
}

