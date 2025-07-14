url = 'http://127.0.0.1:8000/home/search?q='

inp = document.querySelector('.form-control')

inp.addEventListener('input', function(char) {
  url = url + 'char'
  console.log(url)
  get_from_db(url)
});



function get_from_db(url){
  fetch(url)

}