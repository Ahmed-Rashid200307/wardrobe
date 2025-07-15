from django.shortcuts import render, HttpResponse
from .models import Category,Dress,Variant
# Create your views here.

def index(request):
  cat = Category.objects.all()
  dresses = Dress.objects.all()
  print(request.headers)

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