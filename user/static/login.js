
const login_btn = document.getElementById('loginBtn');
const canvas_right = document.getElementById('offcanvasRight');
const form_container = document.getElementById('form-container');
const form_url = login_btn.dataset.url;

async function get_form(){
  
  const res = await fetch(form_url);
  
  const text = await res.text();
  form_container.innerHTML = text;
  canvas_right.dataset.formLoaded = 'true';
}

async function validate_form(form_data) {


  const req = await fetch(form_url,
    {
      method: "POST",
      body: form_data
    }
  );

  if(req.redirected){
    window.location.reload();
  }
  else{

    form_container.innerHTML = res;
  }

}

function add_listner_wform() {

    get_form().then(()=>{

      const form = document.getElementById('form')
      form.addEventListener('submit',(elem)=>{

        elem.preventDefault();
        validate_form(new FormData(form));
      
      });

    }
  )

  canvas_right.removeEventListener('shown.bs.offcanvas',add_listner_wform);

}


canvas_right.addEventListener('shown.bs.offcanvas',add_listner_wform);

export {login_btn}