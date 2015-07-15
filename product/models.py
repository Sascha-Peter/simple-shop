"""This file provides all product related models

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.4.2-alpha
@since: 2015-06-13
"""
from django.db import models


class ProductCategory(models.Model):
    """This class implements the product category model"""
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "product categories"

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """This class implements the product model"""
    product_name = models.CharField(max_length=150)
    product_category = models.ForeignKey(ProductCategory)
    product_price = models.DecimalField(default="00.00", max_digits=10,
                                        decimal_places=2)
    product_stock = models.PositiveIntegerField(default=0)
    slug = models.SlugField()

    def __str__(self):
        return self.product_name
