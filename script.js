// making a post request

let btn = document.querySelector('#post');

let backend = 'https://b493-142-185-241-49.ngrok.io';

var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Access-Control-Allow-Origin", "*")

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