// making a post request

let btn = document.querySelector('#post');

let backend = 'https://b493-142-185-241-49.ngrok.io';

var settings = {
    "url": backend,
    "method": "POST",
    "timeout": 0,
    "headers": {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "application/json"
    },
    "data": JSON.stringify({
        "start_lat": 22,
        "start_lon": 33,
        "end_lat": 55,
        "end_lon": 66
    }),
};

$.ajax(settings).done(function (response) {
    console.log(response);
});

btn.addEventListener('click', function() {
    $.ajax(settings).done(function (response) {
        console.log(response);
    });
})