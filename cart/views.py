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

from djangocart.cart import Cart


def add_to_cart(request, product_id, quantity):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.product_price, quantity)
    messages.add_message(request, messages.SUCCESS,
                         'Item has been added to cart.')
    return HttpResponseRedirect(reverse('product-detail', kwargs={'category_slug': product.product_category.slug, 'slug': product.slug}))


def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    messages.add_message(request, messages.SUCCESS,
                         'Item has been removed from the cart.')
    return HttpResponseRedirect(reverse('product-detail', kwargs={'category_slug': product.product_category.slug, 'slug': product.slug}))


def get_cart(request):
    return render(request, 'cart.html',
                  dict(cart=Cart(request)))
