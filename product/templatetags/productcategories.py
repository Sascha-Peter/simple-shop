"""This file provides custom template tags and filter which
are related to tasks around the product categories

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.1.0-alpha
@since: 2015-06-13
"""
from django import template

from product.models import ProductCategory

register = template.Library()


@register.inclusion_tag('product_categories.html')
def show_male_categories():
    return {'categories': ProductCategory.objects.exclude(category_name__contains="Women's")}

@register.inclusion_tag('product_categories.html')
def show_female_categories():
    return {'categories': ProductCategory.objects.filter(category_name__icontains='Women')}
