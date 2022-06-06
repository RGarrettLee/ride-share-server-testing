const urlParams = new URLSearchParams(window.location.search);
const params = Object.fromEntries(urlParams.entries());

let uberDest = document.querySelector('#dest-uber');
let uberPrice = document.querySelector('#price-uber');
let lyftDest = document.querySelector('#dest-lyft');
let lyftPrice = document.querySelector('#price-lyft');

console.log(params);

uberDest.textContent = params.destination;
lyftDest.textContent = params.destination;

if (params.uberPrice === 'an error occured') {
    uberPrice.textContent = 'Error Please Try Again'
} else {
    uberPrice.textContent = `$${params.uberPrice}`;
}

if (params.lyftPrices === 'an error occured') {
    lyftPrice.textContent = 'Error Please Try Again'
} else {
    uberPrice.textContent = `$${params.lyftPrice}`;
}