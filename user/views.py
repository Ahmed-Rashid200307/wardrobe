from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
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
