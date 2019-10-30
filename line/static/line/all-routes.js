function initMap() {
    //load map where center is myLatLng
    var myLatLng = { lat: 44.2034, lng: 17.9077 };
    map = new google.maps.Map(document.getElementById('map'), {
        center: myLatLng,
        zoom: 8
    });

    //get all json Station data and pares it
    var jsonStationData = document.getElementById('station').innerHTML;
    var allData = JSON.parse(jsonStationData);
    //get all json Line data and pares it
    var jsonLineData = document.getElementById('line').innerHTML;
    var allLines = JSON.parse(jsonLineData);

    //making array of lat lng object pairs and set markers
    //console.log(allData);
    var arrayOfLatLngPairs = [];
    var arrayOfArrayOfLatLngPairs = [];
    for (j = 0; j < allLines.length; j++) {
        for (i = 0; i < allData.length; i++) {
            if (allLines[j].pk === allData[i].fields.line) {
                arrayOfLatLngPairs.push({ lat: Number(allData[i].fields.lat), lng: Number(allData[i].fields.lng) })
                var marker = new google.maps.Marker({
                    position: { lat: Number(allData[i].fields.lat), lng: Number(allData[i].fields.lng) },
                    map: map,
                    icon: {
                        url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
                    }
                });
            }
        }
        arrayOfArrayOfLatLngPairs.push({ val: arrayOfLatLngPairs })
        arrayOfLatLngPairs = [];
    }

    for (i = 0; i < arrayOfArrayOfLatLngPairs.length; i++) {
        arrayOfLatLngPairs.push(arrayOfArrayOfLatLngPairs[i].val);
    }
    //console.log(arrayOfLatLngPairs);
    var routePath = [];
    for (l = 0; l < arrayOfLatLngPairs.length; l++) {
        routePath[l] = new google.maps.Polyline({
            path: arrayOfLatLngPairs[l],
            geodesic: true,
            strokeColor: "#" + ((1 << 24) * Math.random() | 0).toString(16),
            strokeOpacity: 1.0,
            strokeWeight: 2
        });
        routePath[l].setMap(map);
    }

}
