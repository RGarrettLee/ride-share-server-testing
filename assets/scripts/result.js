const urlParams = new URLSearchParams(window.location.search);
const params = Object.fromEntries(urlParams.entries());

let uberDest = document.querySelector('#dest-uber');
let uberPrice = document.querySelector('#price-uber');
let lyftDest = document.querySelector('#dest-lyft');
let lyftPrice = document.querySelector('#price-lyft');

console.log(params);

uberDest.textContent = params.destination;
lyftDest.textContent = params.destination;

if (isNaN(params.uberPrice)) {
    uberPrice.textContent = 'Error Please Try Again'
} else {
    uberPrice.textContent = `$${params.uberPrice}`;
}

if (isNaN(params.lyftPrice)) {
    lyftPrice.textContent = 'Error Please Try Again'
} else {
    uberPrice.textContent = `$${params.lyftPrice}`;
}