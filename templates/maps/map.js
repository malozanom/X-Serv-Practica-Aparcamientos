var map = L.map( 'map', {
  center: [40.418889, -3.691944],   // Centramos el mapa en las coordenadas
  minZoom: 2,                       // de Madrid
  zoom: 11      // Ajustamos el zoom para recoger todos los aparcamientos
});

L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
 attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
 subdomains: ['a','b','c']
}).addTo( map );

var myURL = jQuery( 'script[src$="map.js"]' ).attr( 'src' ).replace( 'map.js', '' );

var myIcon = L.icon({
  iconUrl: myURL + 'pin24.png',     // Cambiamos el icono por defecto y
  iconSize: [29, 24],               // establecemos el tamaño
  iconAnchor: [9, 21],
  popupAnchor: [0, -14]
});

var markerClusters = L.markerClusterGroup();

for ( var i = 0; i < markers.length; ++i )  // Iteramos sobre cada marcadador
{
  var popup = '<a href="' + markers[i].url + '" target="_blank">' + markers[i].name + '</a>'

  var m = L.marker( [markers[i].lat, markers[i].lng], {icon: myIcon} )
                  .bindPopup( popup );

  markerClusters.addLayer( m );
}

map.addLayer( markerClusters );
