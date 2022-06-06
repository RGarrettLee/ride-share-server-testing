// making a post request

let btn = document.querySelector('#post');

let backend = 'https://d979-142-185-241-49.ngrok.io';

var settings = {
    "url": backend,
    "method": "POST",
    "timeout": 0,
    "headers": {
        'Content-Type': 'application/json'
    },
    "data": JSON.stringify({
        "street": 'St Clair Ave E',
        "city": 'Toronto',
        "country": 'CA',
        "postal_code": 'M4T 1P4'
    }),
};

btn.addEventListener('click', function() {
    $.ajax(settings).done(function (response) {
        console.log(response);
    });
})