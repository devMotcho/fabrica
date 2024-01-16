from django.shortcuts import render

from products.models import Product, Production

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
