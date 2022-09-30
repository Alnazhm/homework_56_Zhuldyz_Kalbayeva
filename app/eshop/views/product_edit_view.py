from django.shortcuts import render, redirect
from django.urls import reverse
from eshop.models import Product
from eshop.forms import ProductForm

def product_edit_view(request):
    pass
    # form = ProductForm()
    # if request.method == 'GET':
    #     context = {'form': form}
    #     return render(request, 'add_product.html', context)
    # form = ProductForm(request.POST)
    # if not form.is_valid():
    #     context = {
    #         'form': form
    #     }
    #     return render(request, 'add_product.html', context)
    # product = Product.objects.create(**form.cleaned_data)
    # return redirect(reverse('product_detail', kwargs={'pk': product.pk}))