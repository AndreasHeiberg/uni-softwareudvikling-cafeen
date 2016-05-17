from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseNotAllowed, Http404
from .modules.notifications import Notifications
from .models import ProductGroup, Product, StockCount, StockCountTransaction
from .forms import ProductGroupForm, ProductForm

def methods(methods):
    def real_decorator(func):
        def wrapper(request, *args, **kwargs):
            if request.method in methods:
                return func(request, *args, **kwargs)

            return HttpResponseNotAllowed(methods)
        return wrapper
    return real_decorator

@login_required
@methods(['GET'])
def home(request):
    return render(request, 'stock/home.html', {})

@login_required
@methods(['POST', 'GET'])
def product_groups(request):
    if request.method == 'POST':
        form = ProductGroupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/product-groups')

    if not 'form' in locals():
        form = ProductGroupForm()
        
    groups = ProductGroup.objects.all()
    return render(request, 'stock/product_groups/index.html', {'form': form, 'groups': groups})

@login_required
@methods(['DELETE'])
def product_group(request, id):
    ProductGroup.objects.get(pk=id).delete()
    return redirect('/product-groups')

@login_required
@methods(['POST', 'GET'])
def products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/products')
        
    products = Product.objects.all()
    groups = ProductGroup.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST, groups=groups)
    else:
        form = ProductForm(groups=groups)

    return render(request, 'stock/products/index.html', {'form': form, 'products': products})

@login_required
@methods(['GET', 'PUT', 'DELETE'])
def product(request, id):
    try:
        product = Product.objects.get(pk=id)

        if request.method == 'DELETE':
            product.delete()
            return redirect('/products')

        if request.method == 'PUT':
            product.stock = request.POST['stock']
            product.save()

            return redirect('/products')

        if request.method == 'GET':
            return render(request, 'stock/products/show.html', {'products': products})

    except Product.DoesNotExist:
        raise Http404("Product does not exist")

@login_required
@methods(['POST', 'GET'])
def stock_count(request):
    if request.method == 'POST':
        time = request.POST['time']
        stock_count = StockCount.objects.create(user=request.user)
        differences = []

        for index, stock in request.POST.items():
            if index.endswith('_stock'):
                product_id = index.split('_')[0]
                product = Product.objects.get(pk=product_id)

                if stock != product.stock:
                    differences.append({"product": product, "old": product.stock, "new": stock})

                product.stock = stock
                product.save()

                StockCountTransaction.objects.create(
                    count=stock_count,
                    product_id=product_id,
                    stock=stock
                )

        if time == "pre-shift" and len(differences) > 0:
            subject = "Stock Count Inconsistency"
            sender = 'andreas@heiberg'
            receivers = ['andreas@heiberg.io']
            
            message = "At last stock count at the start of the shift there was an inconsistency with the last stock count. Be adviced:"
            message += "\nname - last count - new count"
            for difference in differences:
                message += "\n" + difference['product'].name + " - " + str(difference['old']) + " - " + str(difference['new'])

            send_mail(subject, message, sender, receivers, fail_silently=False)

            Notifications(request).add('error', message)

        if time == "post-shift":
            turn_over = 0

            for difference in differences:
                turn_over += difference['product'].price * (int(difference['new']) - int(difference['old']))

            Notifications(request).add('success', "Turn over this shift: " + str(turn_over) + "DKK")

        return redirect('/')

    products = Product.objects.all()
    return render(request, 'stock/products/count.html', {'products': products, 'time': request.GET['time']})