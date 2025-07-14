from django.shortcuts import render
from .models import Category,Dress,Variant
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