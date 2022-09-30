from django.shortcuts import render
from eshop.models import Product


def products_view(request):
    products = Product.objects.filter(is_deleted=False)
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)