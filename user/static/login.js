
const link = document.getElementById('login-btn')
const form = document.getElementById('form-container')
const form_url = link.dataset.url + '?'

async function get_form(){
  
  const res = await fetch(form_url)
  
  const text = await res.text();
  form.innerHTML = text
}


document.getElementById('offcanvasRight').addEventListener('shown.bs.offcanvas',()=>{
    get_form()
})


// CREATE POST REQUEST FOR FORM HERE