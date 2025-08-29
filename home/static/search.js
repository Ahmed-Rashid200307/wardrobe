

const inp = document.getElementById('searchInput')
const result = document.querySelector('.search-result')
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
  
  const text = await res.text();
  result.innerHTML = text
}