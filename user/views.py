from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import View
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

class LoginView(View):
  def get(self, request):
    if request.user.isauthenticated:
      return redirect('user:account')
    else:
      form = AuthenticationForm()

      context = {'form': form}
      return render(request,'templates/login.html',context)


  def post(self, request):
    form = AuthenticationForm(request.POST)

    print(request)
