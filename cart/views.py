"""This file provides the views handling cart specific tasks

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.2.0-alpha
@since: 2015-06-13
"""
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

from product.models import Product
from .forms import VoucherUpdateForm

from djangocart.cart import SessionCart
from djangocart.models import Cart


def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = SessionCart(request)
    cart.add(product, product.product_price, quantity)
    messages.add_message(request, messages.SUCCESS,
                         'Item has been added to cart.')
    return HttpResponseRedirect(reverse('product-detail', kwargs={'category_slug': product.product_category.slug, 'slug': product.slug}))


def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = SessionCart(request)
    cart.remove(product)
    messages.add_message(request, messages.SUCCESS,
                         'Item has been removed from the cart.')
    return HttpResponseRedirect(reverse('product-detail', kwargs={'category_slug': product.product_category.slug, 'slug': product.slug}))


def get_cart(request):
    cart_id = request.session.get('CART-ID')
    print(cart_id)
    if request.method == "POST" and cart_id:
        print("we have cart id and post")
        cart = Cart.objects.get(id=cart_id, checked_out=False)
        form = VoucherUpdateForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form = VoucherUpdateForm(request.POST, instance=cart)
            form.save()
            # return HttpResponseRedirect(request.path)
    else:
        form = VoucherUpdateForm()
    return render(request, 'cart.html',
                  dict(cart=SessionCart(request),
                       form=form))
