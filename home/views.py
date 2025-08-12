from django.shortcuts import render, HttpResponse
from .models import Category,Dress,Variant
from django.views.generic import View
from wardrobe import settings
from django.http import FileResponse
# Create your views here.

def index(request):
  dresses = Dress.objects.all()
  
  for dress in dresses:
    print(dress.default_image.url)


  context = {'dresses': dresses}
  return render(request, 'home/index.html', context)


def category(request, cat_id):
  cat = Category.objects.get(id=cat_id)
  dresses = Dress.objects.filter(category=cat)

  context = {'dresses': dresses, 'cat'  : cat}
  return render(request, 'home/cat.html', context)


# Single Product View
class ProductView(View):
  
  # maybe get query from a parameter later
  def get(self,request):

    product = Dress.objects.get(code = request.GET.get('code'))
    category = product.category
    variants = Variant.objects.filter(dress_id = product.pk)
    sizes = product.size.filter(dress = product.pk)


    context = {
      'product': product,
      'code': category.code,
      'variant': variants,
      'sizes' : sizes
    }

    return render(request,'home/detail.html',context)

# Product search service
def search(request):
  search = request.GET.get("q")
  filtered = Dress.objects.filter(name__icontains=search)
  html = """ 
  """
  for dress in filtered:
    html += f"<li class='list-group-item bg-white'>{dress.name}</li>"
  return HttpResponse(html)

# serves images to be displayed for dress or variants
class ImageView(View):
  http_method_names = ['get']

  def get(self, request, type, name):
    
    path = settings.BASE_DIR.joinpath('images',type,name)
    if type == 'default':
      return FileResponse(open(path,'rb'))
    
    elif type == 'variant':
      return FileResponse(open(path,'rb'))
    
    else:
      res = HttpResponse('Invalid request origin')
      res.status_code = 400
      return res
          
