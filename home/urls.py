from django.urls import path,include
from . import views

app_name = 'home'

urlpatterns = [
  path('home/', views.index, name='index'),
  path('home/category/<str:cat_id>', views.category, name='category'),
]
