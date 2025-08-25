const form = document.getElementById('cartForm');


console.log(document.cookie)

async function sendCartInfo() {


    const formData = new FormData(form);
    formData.append('is_login_available', false)

    const validation = await fetch('/cart/validate', {
        method: 'POST',
        body: formData,
    })

    const data = await validation.text()


}

cartBtn.addEventListener('click',sendCartInfo)