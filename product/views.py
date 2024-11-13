from django.shortcuts import render,redirect,get_object_or_404
from .models import Product,CartItem
from .form import ProductForm
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
# Create your views here.

def product_list(request):
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)
    
    # Make sure products exist
    products = Product.objects.all().order_by('id')  # Add order_by to ensure consistent ordering
    
    if not products.exists():
        products = [] 
    
    product_paginator = Paginator(products, 4)
    products = product_paginator.get_page(page)
    
    return render(request, 'shop.html', {'products': products})


def product_details(request, pk):
    try:
        product = get_object_or_404(Product, pk=pk)
        return render(request, 'product_details.html', {'product': product})
    except Product.DoesNotExist:
        return redirect('shop')

@login_required
def add_product(request):
    try:
        form = ProductForm()
        if request.method=='POST':
            form = ProductForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('shop')
            else:
                return render(request, 'product_form.html', {'form': form})
        else:
            form = ProductForm()
            return render(request, 'product_form.html', {'form': form})

    except Exception as e:
        print(e)      
        return render(request, 'product_form.html', {'form': form})



def display(request):
    return render(request,'product_details.html')


@login_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_details', pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, 'update_product.html', {'form': form, 'product': product})


@login_required
def delete_product(request,pk):
    product =Product.objects.get(id=pk)
    
    if request.method == 'POST':
        product.delete()
        return redirect('shop')
        
    else:
        print(product)
        return render(request,'update_product.html',{'product':product})



def shop(request):
    return render(request,'shop.html')


@login_required
def add_cart(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        user=request.user,
        defaults={'quantity': 1},
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')



@login_required
def update_cart(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                product_id = key.split('_')[1]
                try:
                    cart_item = CartItem.objects.get(
                        product_id=product_id,
                        user=request.user
                    )
                    cart_item.quantity = int(value)
                    cart_item.save()
                except CartItem.DoesNotExist:
                    continue  
    return redirect('shop')



def remove_from_cart(request, product_id):
    # Ensure we are attempting to get the specific cart item for this user and product
    cart_item = get_object_or_404(
        CartItem, 
        product_id=product_id,
        user=request.user
    )
    # Delete the matched cart item
    cart_item.delete()
    
    # Redirect to shop page after deletion
    return redirect('shop')


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.quantity * item.product.price for item in cart_items)
    print(cart_items)

    return render(request, 'cart.html', {'cart': cart_items, 'total': total})

