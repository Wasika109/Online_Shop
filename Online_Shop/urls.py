"""Online_Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import demo.views as demo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', demo_views.home_page, name='home'),
    path('about/', demo_views.about_page, name='about'),
    path('products/', demo_views.product_page, name='products'),
    path('cart/', demo_views.cart_page, name='cart'),
    path('reviews/', demo_views.reviews_page, name='reviews'),
    path('drop_ideas/', demo_views.drop_ideas_page, name='drop_ideas'),

]
