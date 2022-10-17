from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse("<h1>This is our home page</h1>")
def about_view(request):
    return HttpResponse("<h1>This is our about page</h1>")

def product_view(request):
    return HttpResponse("<h1>These are our products</h1>")

def cart_view(request):
    return HttpResponse("<h1>This is your cart</h1>")

def reviews_view(request):
    return HttpResponse("<h1>Your Suggestions<h1>")

def drop_ideas_view(request):
    return HttpResponse("<h1?Drop your masterpiece here</h1>")
