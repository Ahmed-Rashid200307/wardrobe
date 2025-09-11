import customerCart  from './cart.js'
import { cartContainer } from './main.js';

const cartBtn = document.getElementById('cartBtn');
const form = document.getElementById('cartForm');
const cartPopup = document.getElementById('cartPopup');


function showAddedPopup(){

    cartPopup.style.right = '30px';
    
    setTimeout(()=>{
        cartPopup.style.right = '-200px'
    }, 4000)
    
}

async function sendCartInfo() {

    const formData = new FormData(form);

    const res = await fetch('/cart/validate', {
        method: 'POST',
        body: formData,
    })

    const data = await res.json()

    if(data.success){
        customerCart.saveItem(formData);
        customerCart.renderProducts(cartContainer);
        showAddedPopup();
    }
    else{
        const login_btn = document.getElementById('loginBtn');
        login_btn.click();
    }




}

cartBtn.addEventListener('click',sendCartInfo)