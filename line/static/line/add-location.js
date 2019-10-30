var map;

function initMap() {

    var myLatLng = { lat: 44.7722, lng: 17.1910 };

    //console.log(myLatLng);

    map = new google.maps.Map(document.getElementById('map'), {
        center: myLatLng,
        zoom: 8
    });


    var marker;

    function placeMarker(location) {
        if (marker) {
            marker.setPosition(location);
        } else {
            marker = new google.maps.Marker({
                position: location,
                map: map
            });
        }
    }




    google.maps.event.addListener(map, 'click', function (event) {
        placeMarker(event.latLng);
        //console.log(event.latLng.lat(), event.latLng.lng())
        var lat = event.latLng.lat();
        var lng = event.latLng.lng();
        lat = lat.toFixed(4);
        lng = lng.toFixed(4);
        console.log(lat, lng);
        p = document.getElementById('demo').innerHTML;
        console.log(p);
        document.getElementById(`id_lat${p}`).value = lat;
        document.getElementById(`id_lng${p}`).value = lng;
    });
} s

function removeLatLng() {
    document.getElementById('id_lat1').value = '';
    document.getElementById('id_lng1').value = '';
}

function selectModal(i) {
    console.log(i);
    document.getElementById("demo").innerHTML = i;
}

