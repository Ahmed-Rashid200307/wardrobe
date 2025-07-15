var url = 'http://127.0.0.1:8000/home/search?'

inp = document.querySelector('.form-control')
result = document.querySelector('.search-result')

inp.addEventListener('input', function() {
  val = inp.value
  if(inp.value){

    get_from_db(url,val)
  }
  else{
    result.innerHTML = ""
  }
});



async function get_from_db(url, param){
  const params = new URLSearchParams()
  params.append("q", param)
  
  const res = await fetch(url+params,{
      method: "GET"
  })
  
  const text = await res.text();
  result.innerHTML = text
  console.log(text);
}