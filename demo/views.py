#from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import authenticate

from django.contrib import messages


from .models import *
from .forms import OrderForm, CreateUserFrom

from django.contrib import messages

# Create your views here.

def home_page(request):
    #return HttpResponse("<h1>This is our home page</h1>")
    return render(request, 'home.html')

def about_page(request):
   # return HttpResponse("<h1>This is our about page</h1>")
 return render(request, 'about.html')

def product_page(request):
   # return HttpResponse("<h1>These are our products</h1>")
   return render(request, 'products.html')
def cart_page(request):
    #return HttpResponse("<h1>This is your cart</h1>")
    return render(request, 'cart.html')
def reviews_page(request):
   # return HttpResponse("<h1>Your Suggestions<h1>")
   return render(request, 'reviews.html')
def drop_ideas_page(request):
   # return HttpResponse("<h1?Drop your masterpiece here</h1>")
   return render(request, 'drop_ideas.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def registration_page(request):
    form = CreateUserFrom()

    if request.method == 'POST':
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'registration.html', context)