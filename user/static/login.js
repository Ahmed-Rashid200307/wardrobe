
const link = document.getElementById('login-btn');
const canvas_right = document.getElementById('offcanvasRight');
const form_container = document.getElementById('form-container');
let form;
const form_url = link.dataset.url;

async function get_form(){
  
  const res = await fetch(form_url);
  
  const text = await res.text();
  form_container.innerHTML = text;
}

async function validate_form(form_data) {


  const req = await fetch(form_url,
    {
      method: "POST",
      body: form_data
    }
  )

  if(req.redirected){
    window.location.replace(req.url)
  }
  else{

    form_container.innerHTML = res
  }
}

function add_listner_wform() {
    get_form().then(
    ()=>{

      form = document.getElementById('form')
      form.addEventListener('submit',(elem)=>{

        elem.preventDefault()
        validate_form(new FormData(form));
      
      });

    }
  )

  canvas_right.removeEventListener('shown.bs.offcanvas',add_listner_wform)

}


canvas_right.addEventListener('shown.bs.offcanvas',add_listner_wform);