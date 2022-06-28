
 limparCampos();

//classe central da API usada para criar o mapa
var mapao = L.map('map', {center: [-20.718637820756296,-47.880477905273445], zoom:17})


//carrega camadas de apresentação sobre o mapa
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mapao);


//cria instãncia de janela modal
const elem = document.getElementById('cadCoord');
const modalCordenada = M.Modal.init(elem, {dismissible:false});


var item = new Array();

mapao.on("dblclick", function (event) {
  //console.log("user right-clicked on map coordinates: " + event.latlng.toString());

  if (item.length < 1){

    item.push(L.marker(event.latlng).addTo(mapao));
    mostrarCoordenadas();
    modalCordenada.open();


  }
  else {
    alert("Somente é possível " + item.length +" coordenada(s) por vez!")
  }
});

//mostra coordenadas sobre o mapa no formato lat, long como entradas somente leitura
function mostrarCoordenadas(){
//  var entradas = "";
//  for (i=0; i<item.length; i++){
//      let lat =item[i]._latlng.lat.toString();
//      let lon = item[i]._latlng.lng.toString();
//      entradas = entradas + "<input type='text' value="+lat+" name='coords"+ lat +"' readonly/>";
//      entradas = entradas + "<input type='text' value="+lon+" name='coords"+ lon+"' readonly/>";
//      entradas = entradas +"<input type='text' name='descCoords"+ i.toString()+"' placeholder='Endereço do Ponto'/> <br>";
// 		  console.log(item[i]._latlng);
//  }
//
//  coordenadas.innerHTML = entradas + "<input type='submit'>";
  for (i=0; i<item.length; i++) {
       let lat = item[i]._latlng.lat.toString();
       let lon = item[i]._latlng.lng.toString();
       latitude.value=lat;
       longitude.value=lon;
  }


}

// Deleta primeira coordenada do mapa
function delDoPrimeiro() {

  if (item.length !== 0){
     mapao.removeLayer(item.shift());
     mostrarCoordenadas();
     modalCordenada.close();
     limparCampos();
  }
}

function limparCampos() {
  document.getElementById('id_des').value='';
  document.getElementById('id_hr').value='';
  document.getElementById('id_min').value='';
}

deletar.addEventListener("click", function(){
    delDoPrimeiro();
});

//        // formata objeto JSON
//        for (i =0; i < texto.length; i++){
//            if (( i != 0) && ( i != (texto.length-1)) ){
//                if (texto[i] === '\'') {
//
//                    obj = obj + '\"';
//                 }
//                else {
//                    obj = obj + texto[i];
//                }
//            }
//        }


carregaPontos();

function carregaPontos(){

        // Pega coordenadas da div
        var obj = coord.innerHTML;

        if (obj !== ''){
            // converte para objeto
            const obj_json = JSON.parse(obj);
            //carrega ponto no mapa
            for (let i in obj_json.pontos){
               L.marker([parseFloat(obj_json.pontos[i].lat), parseFloat(obj_json.pontos[i].long)],{fillColor:'green'})
               .addTo(mapao)
               .bindPopup(obj_json.pontos[i].trajeto.toString());
               //.openPopup();
            }
        }
}


function gravarPonto () {
    document.getElementById('coordenadas').submit();
    
}

getLocation();

function getLocation() {


  //https://www.w3schools.com/js/js_api_geolocation.asp
  if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition(posicaoUsuario)
  }

}

function posicaoUsuario(posicao) {


  L.marker([parseFloat(posicao.coords.latitude),parseFloat(posicao.coords.longitude)])
  .addTo(mapao)
  .bindPopup('Você aqui')
  .openPopup();
}

