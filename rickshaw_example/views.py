from django.shortcuts import render
from .models import Product
from rickshaw.shared.service import RickshawService

def app(request):
    products = Product.objects.all()
    RickshawService(request)
    return render(request, "index.html", {'products': products})

def addtocart(request):
    product = Product.objects.get(id=request.GET.get('product', ''))
    rickshaw = RickshawService(request)
    rickshaw.add_cargo(product, int(request.GET.get('quantity', 1)))
    hold = rickshaw.cargo_hold()
    total = rickshaw.cargo_value()
    return render(request, 'cart.html', {'hold':hold, 'total': total })
