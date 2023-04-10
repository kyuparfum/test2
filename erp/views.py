from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from quantity.models import QuantityModel
from .forms import *
from django.contrib import messages
from django.contrib.auth import get_user_model


# Create your views here.
# @login_required
def inventory(request):
    user = request.user.is_authenticated
    if user:
        products = ProductModel.objects.filter(author_id=request.user)
        return render(request, 'erp/inventory.html', {'products': products})
    else:
        return redirect('/login')


def create_product(request):
    user = request.user.is_authenticated
    if not user:
        return redirect('/login/')
    else:
        if request.method == 'POST':
            form_check = ProductForm(request.POST)
            if form_check.is_valid():
                exist_user = get_user_model().objects.filter(username=request.user)
                if exist_user:
                    form = request.POST
                    product = ProductModel()
                    product.code = form['code']
                    product.author = request.user
                    product.name = form['name']
                    product.price = form['price']
                    product.description = form['description']
                    product.t_size = form['t_size']
                    product.quantity = form['quantity']
                    product.save()
                    messages.success(request, '제품등록성공.')
                    return redirect('/inventory')
        elif request.method == 'GET':
            user = request.user.is_authenticated
            if user:
                form = ProductForm()
                return render(request, 'erp/create_product.html', {'form': form})


def inventory_detail(request, id):
    if request.method == 'GET':
        my_product = ProductModel.objects.get(id=id)
        my_inventory_form = InventoryForm()
        my_inventory_delete_form = InventoryDeleteForm
        my_inventory = InventoryModel.objects.filter(author_id=request.user, product_id=id)
        my_delete_inventory = QuantityModel.objects.filter(author_id=request.user, product_id=id)
        test = QuantityModel.objects.filter(author_id=request.user, product_id=id)
        total = 0
        for i in my_inventory:
            total += i.total
        for j in my_delete_inventory:
            total -= j.decreased
        return render(request, 'erp/inventory_detail.html', {'product': my_product,
                                                             'total': total,
                                                             'form': my_inventory_form,
                                                             'delete': test,
                                                             'deleteform': my_inventory_delete_form,
                                                             'inventory': my_inventory})
    elif request.method == 'POST':
        my_inventory = InventoryModel()
        my_inventory.product = ProductModel.objects.get(id=id)
        my_inventory.author = request.user
        form = request.POST
        my_inventory.total = form['total']
        my_inventory.decreased = 0
        my_inventory.save()
        return redirect(f'/inventory/{id}')


def inventory_delete(request, id):
    my_inventory = InventoryModel.objects.filter(author_id=request.user, product_id=id)
    my_delete_inventory = QuantityModel.objects.filter(author_id=request.user, product_id=id)
    total = 0
    for i in my_inventory:
        total += i.total
    for j in my_delete_inventory:
        total -= j.decreased
    form =request.POST
    my_quantity = QuantityModel()
    my_quantity.author = request.user
    my_quantity.product = ProductModel.objects.get(id=id)
    my_quantity.decreased = form['total']
    if total >= int(my_quantity.decreased):
        my_quantity.save()
        return redirect(f'/inventory/{id}')
    else:
        print('재고부족')
        return redirect(f'/inventory/{id}')