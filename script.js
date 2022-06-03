// making a post request

let btn = document.querySelector('#post');

let backend = 'https://b493-142-185-241-49.ngrok.io';

var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "start_lat": 22,
  "start_lon": 33,
  "end_lat": 55,
  "end_lon": 66
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

btn.addEventListener('click', function() {
    fetch("https://b493-142-185-241-49.ngrok.io", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
})

/*function sendPost() {
    fetch(backend, {
        method: 'POST',
        mode: 'no-cors',
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

btn.addEventListener('click', sendPost)*/