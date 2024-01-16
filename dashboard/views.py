from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product, Production

@login_required(login_url='users:login')
def dashboardView(request):
    products = Product.objects.filter()
    products_count = products.count()

    productions = Production.objects.filter()
    productions_count = productions.count()

    context = {
        'products':products,
        'products_count':products_count,
        'productions_count':productions_count,
    }
    return render(request, 'dashboard/home.html', context)
