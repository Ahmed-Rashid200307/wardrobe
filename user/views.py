from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import View,FormView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate
# Create your views here.

def register(request):
  if request.method != 'POST':
    form = UserCreationForm()
  else:
    form = UserCreationForm(request.POST)

    if form.is_valid():
      user = form.save()
      login(request, user)
      redirect('home:index')

  context = {'form': form}
  return render(request, 'registration/register.html', context)

def account(request):
  
  return render(request, 'registration/account.html')

class LoginView(FormView):
  template_name = 'login.html'
  # def get(self, request):
  #   print(request.headers['Cookie'])
  #   print(request.COOKIES)
  #   num_visits = request.session.get('num_visits', 0)
  #   request.session['num_visits'] = num_visits + 1
  #   print(num_visits)
  #   form = AuthenticationForm()

  #   context = {'form': form}

  #   return render(request,'templates/user/login.html',context)


  # def post(self, request):
  #   # form = AuthenticationForm(request.POST)

  #   print(request)
