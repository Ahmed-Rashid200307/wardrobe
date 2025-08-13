from django.urls import path, include
from . import views
app_name = "user"

urlpatterns = [
  path('cart/', views.Cart.as_view()),
  path('checkout/', views.Cart.as_view())
]