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

        p = document.getElementById('demo').innerHTML;
        document.getElementById(`id_lat${p}`).value = Number(lat.toFixed(4));
        document.getElementById(`id_lng${p}`).value = Number(lng.toFixed(4));
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

