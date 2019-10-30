function initMap() { }

jQuery(document).ready(function () {
    myFunction();
    var i = 2;
    jQuery('#add').click(function (e) {
        e.preventDefault()
        jQuery('#items').append(`<div><label for="id_station_name">Station name:</label>&nbsp<input type="text" name="station_name" maxlength="30" required="" id="id_station_name">&nbsp<label for="id_lat">Lat:</label>&nbsp<input type="number" name="lat" step="0.0001" required="" id="id_lat${i}">&nbsp<label for="id_lng">Lng:</label>&nbsp<input type="number" name="lng" step="0.0001" required="" id="id_lng${i}">&nbsp<button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-target="#myModal" onclick="selectModal(${i})" value =${i}">&nbspOpen GoogleMap</button>&nbsp<input type="button" value="Delete" class="btn btn-danger" id="delete"></div>`);
        i = i + 1;
    });


    jQuery('body').on('click', '#delete', function (e) {
        e.preventDefault();
        jQuery(this).parent('div').remove();
    });
});
function myFunction() {
    for (i = 0; i < 2; i++) {
        jQuery('#items').append(`<div><label for="id_station_name">Station name:</label>&nbsp<input type="text" name="station_name" maxlength="30" required="" id="id_station_name">&nbsp<label for="id_lat">Lat:</label>&nbsp<input type="number" name="lat" step="0.0001" required="" id="id_lat${i}">&nbsp<label for="id_lng">Lng:</label>&nbsp<input type="number" name="lng" step="0.0001" required="" id="id_lng${i}">&nbsp<button type="button" class="btn btn-info btn-sm" data-toggle="modal" data-target="#myModal" onclick="selectModal(${i})" value =${i}">&nbspOpen GoogleMap</button>&nbsp</div>`);
    }
}
