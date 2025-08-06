from django.urls import path,include
from . import views

app_name = 'home'

urlpatterns = [
  path('', views.index, name='index'),
  path('images/<str:type>/<str:name>/', views.ImageView.as_view(), name='images'),
  path('home/category/<str:cat_id>', views.category, name='category'),
  path('home/product/',views.ProductView.as_view(), name='products'),
  path('home/search/', views.search, name='search'),
]
