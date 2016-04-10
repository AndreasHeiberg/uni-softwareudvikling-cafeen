from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ProductGroup, Product, StockCount, StockCountTransaction
from django.core.mail import send_mail
from django.http import HttpResponse
from .modules.notifications import Notifications

@login_required
def home(request):
    return render(request, 'stock/home.html', {})

@login_required
def product_groups(request):
    if request.method == 'POST':
        ProductGroup.objects.create(name=request.POST['name'])
        return redirect('/stock/product-groups')

    groups = ProductGroup.objects.all()
    return render(request, 'stock/product_groups/index.html', {'groups': groups})

@login_required
def product_group(request, id):
    if request.method == 'DELETE':
        ProductGroup.objects.get(pk=id).delete()
        return redirect('/stock/product-groups')

@login_required
def products(request):
    if request.method == 'POST':
        group = ProductGroup.objects.get(pk=request.POST['group_id'])
        Product.objects.create(
            name=request.POST['name'],
            group_id=group,
            price=int(request.POST['price']),
            price_rent=int(request.POST['price_rent'])
        )
        return redirect('/stock/products')

    products = Product.objects.all()
    groups = ProductGroup.objects.all()
    return render(request, 'stock/products/index.html', {'products': products, 'groups': groups})

@login_required
def product(request, id):
    if request.method == 'DELETE':
        Product.objects.get(pk=id).delete()
        return redirect('/stock/products')

    if request.method == 'PUT':
        try:
            product = Product.objects.get(pk=id)
            product.stock = request.POST['stock']
            product.save()

            return redirect('/stock/products')
        except Product.DoesNotExist:
            # handle error or exception handle?
            return redirect('/stock/products')

@login_required
def stock_count(request):
    if request.method == 'POST':
        time = request.POST['time']
        stock_count = StockCount.objects.create(user_id=request.user)
        differences = []

        for index, count in request.POST.items():
            if index.endswith('_stock'):
                product_id = index.split('_')[0]
                product = Product.objects.get(pk=product_id)

                if count != product.stock:
                    differences.append({"product": product, "old": product.stock, "new": count})

                product.stock = count
                product.save()

                StockCountTransaction.objects.create(
                    count_id=stock_count,
                    product_id=product,
                    count=count
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

        return redirect('/stock')

    products = Product.objects.all()
    return render(request, 'stock/products/count.html', {'products': products, 'time': request.GET['time']})