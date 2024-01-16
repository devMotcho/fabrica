from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from django.forms import formset_factory
from django.forms.models import modelformset_factory

from django.db.models import Q

from .models import Product, Inventary, Production
from .forms import ProductForm, ProductionForm, BaseProductionFormSet


# Produtos
class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('q')  # Obtém o parâmetro de consulta da URL
        object_list = Product.objects.all()

        if query:
            # Filtra os produtos pelo nome ou categoria usando Q objects
            object_list = object_list.filter(Q(name__icontains=query) | Q(category__icontains=query))

        return object_list


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product has been created!', "alert-success alert-dismissible")
        else:
            messages.error(request, 'Create Product failed!', "alert-danger alert-dismissible")
        return self.get(request, *args, **kwargs)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product Deleted!', "alert-success alert-dismissible")
        return redirect('products:products')
    return render(request, 'products/delete.html', {'obj': product})

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Updated!', "alert-success alert-dismissible")
            return redirect('products:products')

    context = {
        'form':form,
        'product':product,

    }
    return render(request, 'products/update.html', context)

# Inventario
def viewInventary(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    inv = Inventary.objects.filter(
        Q(product__name__icontains=q)
    )


    context = {
        'inv' : inv,

    }
    return render(request, 'products/inventary.html', context)


# Produção
def viewProduction(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    productions = Production.objects.filter(
        Q(operator__first_name__icontains=q) |
        Q(product__name__icontains=q)
    )
        # Criação do formset com base no formulário do modelo Production
    ProductionFormSet = modelformset_factory(Production, ProductionForm, extra=1, formset=BaseProductionFormSet)

    formset = ProductionFormSet(queryset=Production.objects.none())

    if request.method == 'POST':
        form = ProductionFormSet(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:productions')

            messages.success(request, 'Productions added with success!', "alert-success alert-dismissible")


    context = {
        'productions': productions,
        'formset':formset,
    }

    return render(request, 'products/production.html', context)

def editProduction(request, pk):
    production = Production.objects.get(id=pk)
    form = ProductionForm(instance=production)

    if request.method == 'POST':
        form = ProductionForm(request.POST, instance=production)
        if form.is_valid():
            form.save()
            messages.success(request, 'Production Updated!', 'alert-success alert-dismissible')
            return redirect('products:productions')
        else:
            messages.error(request, 'Something went wrong!', 'alert-warning alert-dismissible')

    context = {
        'form':form
    }

    return render(request, 'products/edit.html', context )




