from django.shortcuts import render

from .models import ProductCategory, Product


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'GeekShop Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    context = {
        'title': 'GeekShop - Каталог',
        'header': 'GeekShop',
        'categories': categories,
        'products': products,
    }
    return render(request, 'products/products.html', context)
