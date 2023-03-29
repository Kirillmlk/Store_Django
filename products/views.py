from django.shortcuts import render
from products.models import ProductCategory, Product

from django.core.paginator import Paginator


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page_number=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)

    context = {'title': 'Store - Каталог',
               'categories': ProductCategory.objects.all(),
               'products': products_paginator,
               }
    return render(request, 'products/products.html', context)
