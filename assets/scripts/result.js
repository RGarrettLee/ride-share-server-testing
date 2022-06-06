const urlParams = new URLSearchParams(window.location.search);
const params = Object.fromEntries(urlParams.entries());

let uberDest = document.querySelector('#dest-uber');
let uberPrice = document.querySelector('#price-uber');
let lyftDest = document.querySelector('#dest-lyft');
let lyftPrice = document.querySelector('#price-lyft');

let errorMessage = 'An error occured';

uberDest.textContent = params.destination;
lyftDest.textContent = params.destination;

if (isNaN(params.uberPrice)) {
    uberPrice.textContent = errorMessage;
} else {
    uberPrice.textContent = `$${params.uberPrice}`;
}

if (!isNaN(params.lyftPrice)) {
    lyftPrice.textContent = errorMessage;
} else {
    lyftPrice.textContent = `$${params.lyftPrice}`;
}