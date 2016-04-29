from django.shortcuts import render, redirect
from .models import ProductGroup, Product

def home(request):
    return render(request, 'stock/home.html', {})

def product_groups(request):
    if request.method == 'POST':
        ProductGroup.objects.create(name=request.POST['name'])
        return redirect('/product-groups')

    groups = ProductGroup.objects.all()
    return render(request, 'stock/product_groups/index.html', {'groups': groups})

def product_group(request, id):
    if request.method == 'DELETE':
        ProductGroup.objects.get(pk=id).delete()
        return redirect('/product-groups')

def products(request):
    if request.method == 'POST':
        group = ProductGroup.objects.get(pk=request.POST['group_id'])
        Product.objects.create(
            name=request.POST['name'],
            group_id=group,
            price=int(request.POST['price']),
            price_rent=int(request.POST['price_rent'])
        )
        return redirect('/products')

    products = Product.objects.all()
    groups = ProductGroup.objects.all()
    return render(request, 'stock/products/index.html', {'products': products, 'groups': groups})

def product(request, id):
    if request.method == 'DELETE':
        Product.objects.get(pk=id).delete()
        return redirect('/products')

    if request.method == 'PUT':
        try:
            product = Product.objects.get(pk=id)
            product.stock = request.POST['stock']
            product.save()

            return redirect('/products')
        except Product.DoesNotExist:
            # handle error or exception handle?
            return redirect('/products')