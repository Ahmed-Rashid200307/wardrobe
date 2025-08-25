from django.urls import path, include
from . import views

app_name = "transact"

urlpatterns = [
  path('cart/validate', views.CartAction.as_view(), name='cartValidate')
]