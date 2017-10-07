/** a const containing metadata for each weather condition:
 * ['icon_url', 'image_url', 'image_alt'] */
const weatherCondition = {
    'clear sky': ['01d', 'clear_sky', 'Clear Sky'],
    'few clouds': ['02d', 'few_clouds', 'Few Clouds'],
    'scattered clouds': ['03d', 'scattered_clouds', 'Scattered Clouds'],
    'broken clouds': ['04d', 'broken_clouds', 'Broken Clouds'],
    'shower rain': ['09d', 'shower_rain', 'Shower Rain'],
    'rain': ['10d', 'rain', 'Rain'],
    'thunderstorm': ['11d', 'thunderstorm', 'Thunderstorm'],
    'snow': ['13d','snow', 'Snow'],
    'mist': ['50d','mist','Mist']
};

// base url for our images
const imageUrl = 'img/'; // remember to add .jpeg

// base url for our icons
const iconUrl = 'http://openweathermap.org/img/w/'; // remember to add .png

// Openweather's API key - bad practice to leave it here but that will do for this project's purpose
const apiKey = 'xxxxxxxxxxx';

// Global var to store the temp, not the best practice but will do for this mini project
var current_temp;

// Global var to store weather condition, same as above, not the best design
var current_condition;

// Ask the user to accept geo location request access, if he declines, pop an alert box
$(document).ready(function() {
        navigator.geolocation.getCurrentPosition(userAccepted, userDenied);
            $('#toggle_button').on('click', function () {
        $('p.mid_temp').toggleClass('cel');
        $('p.mid_temp').toggleClass('fah');

        if ($('p.mid_temp').hasClass('cel')) {
            $('p.mid_temp').text("Current Temp: " + Math.round(((current_temp - 32) / 1.8) * 100) / 100 + "C");
         return;
        }
        $('p.mid_temp').text("Current Temp: " + current_temp + "F");

});
});

function userAccepted(pos) {
    $("#above_main").append('<div class="alert alert-info"> Location Services Enabled </div>');
    let lat_value = pos.coords.latitude;
    let long_value = pos.coords.longitude;

    $.ajax( {
        url: 'http://api.openweathermap.org/data/2.5/weather?' + 'lat=' + lat_value + '&lon=' + long_value + '&appid=' +
            apiKey + '&units=imperial',
        success: [function(myData) {
            current_temp = myData['main']['temp'];
            current_condition = myData['weather'][0]['description'];
            let current_city = myData['name'];
            getTemps(lat_value, long_value, current_temp, current_city, current_condition);
            returnCond(current_condition);
        }]
        }
    );
}


function userDenied() {
    $("#above_main").append('<div class="alert alert-danger" id="decline_alert"> Location Services Disabled </div>');
    $("#current_latitude").text("Latitude: " + "N/A");
    $("#current_longitude").text("Longitude: " + "N/A");
    $("#current_city").text("Current City: " + "N/A")
    $("p.mid_temp").text("Current Temp: " + "N/A");
    $("#toggle_button").prop('disabled', true);

    // Uncomment below to auto remove the alert box from the DOM
    // setTimeout(function () {
    // $('#decline_alert').remove();
    // }, 5000);
}


// Call to retrieve current temp based on latitude and longitude values
function getTemps(latValue, longValue, tempValue, currentCity) {
    $("#current_latitude").text("Latitude: " + latValue);
    $("#current_longitude").text("Longitude: " + longValue);
    $("p.mid_temp").text("Current Temp: " + tempValue + "F");
    $("#current_city").text("Current City: " + currentCity);
}

function returnCond(currCond) {
    $('#main_container').css('background-image', 'url('+imageUrl+weatherCondition[currCond][1]+'.jpg)');
    $('#temp_icon').attr('src', iconUrl+weatherCondition[currCond][0]+'.png')
}
