

from django.shortcuts import render
from .models import Laptop

def home(request):
    laptops = Laptop.objects.all().order_by('-id')

    brands = Laptop.objects.values_list(
        'brand', flat=True
    ).distinct()

    return render(request, 'index.html', {
        'laptops': laptops,
        'brands': brands,
    })
