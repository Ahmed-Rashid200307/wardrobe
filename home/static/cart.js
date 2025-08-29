import {login_btn} from './login.js'
const form = document.getElementById('cartForm');


console.log(document.cookie)

async function sendCartInfo() {


    const formData = new FormData(form);

    const res = await fetch('/cart/validate', {
        method: 'POST',
        body: formData,
    })

    const data = await res.json()

    if(data.success){
        console.log('added to cart')
    }
    else{
        login_btn.click();
    }




}

cartBtn.addEventListener('click',sendCartInfo)
var cred = new CredentialsContainer()
console.log(cred.get())