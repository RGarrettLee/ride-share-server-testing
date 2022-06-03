// making a post request

let btn = document.querySelector('#post');

let backend = 'https://b493-142-185-241-49.ngrok.io';

function sendPost() {
    fetch(backend, {
        method: 'POST',
        headers: {
            'Content-Type': 'Authorization',
            'Accept': '*/*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'x-requested-with',
            'Access-Control-Allow-Origin': backend
        },
        body: {
            'start_lat': 55,
            'start_lon': 33,
            'end_lat': 22,
            'end_lon': 11
        }
    })
}

function xml() {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', backend);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            console.log(xhr.status);
            console.log(xhr.responseText);
        }
    }

    let data = '{"start_lat": 22, "start_lon": 11, "end_lat": 55, "end_lon": 77}';

    xhr.send(data);
}

let invocation = new XMLHttpRequest();

function call() {
    if (invocation) {
        invocation.open('POST', backend, true);
        invocation.setRequestHeader('Content-Type', 'application/json');
        invocation.setRequestHeader('Accept', '*/*');
        invocation.setRequestHeader('Accept-Encoding', 'gzip, deflate, br');
        invocation.setRequestHeader('Connection', 'keep-alive');
        let data = '{"start_lat": 22, "start_lon": 11, "end_lat": 55, "end_lon": 77}';
        invocation.send(data);
    }
}

btn.addEventListener('click', function() {
    /*$.post(backend, {start_lat: 22, start_lon: 33, end_lat: 55, end_lon: 77}, function() {
        console.log('posted');
    }, 'json'); */
    $.ajax(backend, {
        type: 'POST',
        dataType: 'json',
        data: {start_lat: 22, start_lon: 33, end_lat: 55, end_lon: 77},
        success: function() {console.log('success')},
        error: function() {console.log('failed')}
    })
});