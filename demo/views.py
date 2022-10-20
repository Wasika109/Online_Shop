from django.shortcuts import render, HttpResponse

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