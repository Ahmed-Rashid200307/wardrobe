from django.shortcuts import render, HttpResponse
from .models import Category,Dress,Variant
from django.views.generic import View
from wardrobe import settings
from django.http import FileResponse
# Create your views here.

def index(request):
  cat = Category.objects.all()
  dresses = Dress.objects.all()
  

  context = {'category': cat,
             'dresses': dresses}
  return render(request, 'home/index.html', context)


def category(request, cat_id):
  cat = Category.objects.get(id=cat_id)
  dresses = Dress.objects.filter(category=cat)

  context = {'dresses': dresses}
  return render(request, 'home/cat.html', context)

def search(request):
  search = request.GET.get("q")
  filtered = Dress.objects.filter(name__icontains=search)
  html = """ 
  """
  for dress in filtered:
    html += f"<li>{dress.name}</li>"
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
          
