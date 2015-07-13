"""This file provides all views related to product categories
and products. Mainly the display and interaction of said functions.

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.3.0-alpha
@since: 2015-06-13
"""
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ProductCategory, Product


class ProductCategoryList(ListView):
    """Generic list view for product categories"""
    model = ProductCategory
    template_name = "product/productcategory_list.html"

    def get_queryset(self):
        """Custom queryset to return related products in category"""
        return Product.objects.filter(product_category__slug=self.kwargs['slug'])


class ProductDetailView(DetailView):
    """Generic detail view for a product"""
    model = Product
