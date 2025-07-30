from django.urls import path, include
from . import views
app_name = "user"

urlpatterns = [
  path("", include("django.contrib.auth.urls")),
  path("register/", views.register, name='register'),
  path("account/", views.account, name='account'),
  path('login/', views.LoginView.as_view(), name='login'),
]