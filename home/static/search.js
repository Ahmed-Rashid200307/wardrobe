

const inp = document.getElementById('searchInput')
const result = document.getElementById('searchResult')
const url = inp.dataset.url + '?'

inp.addEventListener('input', function() {
  const val = inp.value
  if(inp.value){

    get_from_db(url,val)
  }
  else{
    result.innerHTML = ''
  }
});

function remove_list(e) {
  if((e.target == inp) || (e.target == result)){
    result.style.display = 'block';
  }else {
    result.style.display = 'none';
  }
}

document.addEventListener('click', remove_list)


async function get_from_db(url, param){

  const params = new URLSearchParams()
  params.append("q", param)
  
  const res = await fetch(url+params,{
      method: "GET",
  })
  
  const data = await res.json();
  
  if(data){
    fillData(data)
  }
}

function fillData(data){

  let html = '';

  Object.entries(data).forEach(([key, value]) => {

    if(value.length != 0){
      html += `
          <div class="col-6 border-end pe-3" id="${key}-container">
          
            <h6 class="fw-bold">${key}</h6>

            <ul class="list-unstyled mb-0" id="${key}-results">
      `

      value.forEach(item =>{
        html += `
          <li>
            <a href="/category/${item[1]}" 
            class="text-decoration-none d-block py-1 text-dark">
            ${item[0]}
            </a>
          </li>
        `
      })

      html += `
        </ul>
        </div>
      `
        
    }
  });

  result.innerHTML = html
}