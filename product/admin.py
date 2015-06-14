"""This file contains all the product related admin definitions

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.2.0-alpha
@since: 2015-06-13
"""
from django.contrib import admin

from .models import ProductCategory, Product


class ProductCategoryAdmin(admin.ModelAdmin):
    """Defines the model admin for product categories"""
    model = ProductCategory
    prepopulated_fields = {"slug": ("category_name",)}


class ProductAdmin(admin.ModelAdmin):
    model = Product
    prepopulated_fields = {"slug": ("product_name",)}

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
