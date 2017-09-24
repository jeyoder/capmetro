
function show_alert(text) {
    $('nav').after('<div class="alert alert-success alert-dismissible" role="alert">' 
        + '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
          '<span aria-hidden="true">&times;</span></button>'
        + text + '</div>');
}

var socket = io.connect('http://' + document.domain + ':' + location.port);

function initMap() {
    var uluru = {lat: -25.363, lng: 131.044};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: uluru
    });
    var marker = new google.maps.Marker({
        position: uluru,
        map: map
    });
}
