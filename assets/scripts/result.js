const urlParams = new URLSearchParams(window.location.search);
const params = Object.fromEntries(urlParams.entries());

let uberDest = document.querySelector('#dest-uber');
let uber_price = document.querySelector('#price-uber');
let lyftDest = document.querySelector('#dest-lyft');
let lyft_price = document.querySelector('#price-lyft');

uberDest.textContent = params.destination;
lyftDest.textContent = params.destination;

uber_price = params.uberPrice;
lyft_price = params.lyftPrice;