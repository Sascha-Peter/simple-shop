"""This file contains all the product related admin definitions

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.1.0-alpha
@since: 2015-06-13
"""
from django.contrib import admin

from .models import ProductCategory, Product


class ProductCategoryAdmin(admin.ModelAdmin):
    """Defines the model admin for product categories"""
    model = ProductCategory


class ProductAdmin(admin.ModelAdmin):
    model = Product

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
