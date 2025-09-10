import {cart } from './cart.js'
const customerCart = new cart('wardrobeCart');
customerCart.loadFromStorage();

const cartBtn = document.getElementById('cartBtn');
const form = document.getElementById('cartForm');
const cartPopup = document.getElementById('cartPopup');
const cartContainer = document.getElementById('cartContainer');

function showAddedPopup(){

    cartPopup.style.right = '30px';
    
    setTimeout(()=>{
        cartPopup.style.right = '-200px'
    }, 4000)
    
}

// function addProductToSideBar(){
    
//     let cartContainer = document.getElementById('cartContainer');
    
//     cartContainer.innerHTML += `
//         <div id="itemContainer" class="col">
//             <div class="row row-cols-3">
//               <div class="col px-4 pb-4">
//                 <img class="image-fluid w-75" id="itemImage" src="/static/images/${cart.get('productColor')}" alt="">
//               </div>
//               <div class="col">
//                 <p id="itemName">${cart.get('productName')}</p>
//               </div>
//               <div class="col">
//                 <p id="Quantity">${cart.get('productQuantity')}</p>
//               </div>
//             </div>
//         </div>
//     `

// }

async function sendCartInfo() {

    const formData = new FormData(form);

    const res = await fetch('/cart/validate', {
        method: 'POST',
        body: formData,
    })

    const data = await res.json()

    if(data.success){
        customerCart.saveItem(formData);
        customerCart.addProductToElement(cartContainer);
        showAddedPopup();
    }
    else{
        const login_btn = document.getElementById('loginBtn');
        login_btn.click();
    }




}

cartBtn.addEventListener('click',sendCartInfo)
customerCart.addProductToElement(cartContainer);