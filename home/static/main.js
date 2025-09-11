import customerCart from './cart.js';


const cartContainer = document.getElementById('cartContainer');
customerCart.renderProducts(cartContainer);


export {cartContainer}