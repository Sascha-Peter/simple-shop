"""This file contains all tests for the product module.

@author: Sascha Peter <sascha.o.peter@gmail.com>
@version: 0.5.0-alpha
@since: 2015-07-13
"""
from django.test import Client, TestCase, RequestFactory
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from .models import Product, ProductCategory


class ProductCategoryTestCase(TestCase):
    """Test case for product categories"""
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        """Testing if a skill category, after creation, is displayed
        on the homepage
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_product_category(self):
        """Test if product categories are properly created on homepage"""
        ProductCategory.objects.create(category_name="Men's Shoeware",
                                       slug=slugify("Men's Shoeware"))
        response = self.client.get(reverse('home'))
        self.assertEqual(len(response.context['categories']), 1)

    def test_multiple_product_categories(self):
        """Test if multiple product categories are properly created
        on homepage
        """
        ProductCategory.objects.create(category_name="Men's Casualwear",
                                       slug=slugify("Men's Casualwear"))
        ProductCategory.objects.create(category_name="Men's Formalwear",
                                       slug=slugify("Men's Formalwear"))
        response = self.client.get(reverse('home'))
        self.assertEqual(len(response.context['categories']), 2)

    def test_product_category_list_view_empty(self):
        """Tests if an empty product category list is displayed"""
        response = self.client.get(reverse('product-list',
                                           kwargs={'slug': 'mens-formalwear'}))
        self.assertEqual(response.status_code, 200)

    def test_product_category_list_view_with_products(self):
        """Tests if a product category page with 3 items is propperly recognised"""
        product_category = ProductCategory.objects.create(category_name="Men's Formalwear",
                                                          slug=slugify("Men's Formalwear"))
        Product.objects.create(product_name="Fine Stripe Short Sleeve Shirt, Green",
                               product_category=product_category,
                               product_price="34.00",
                               product_stock=12,
                               slug=slugify("Fine Stripe Short Sleeve Shirt, Green"))
        Product.objects.create(product_name="Fine Stripe Short Sleeve Shirt, Grey",
                               product_category=product_category,
                               product_price="12.00",
                               product_stock=12,
                               slug=slugify("Fine Stripe Short Sleeve Shirt, Grey"))
        Product.objects.create(product_name="Fine Stripe Long Sleeve Shirt, Green",
                               product_category=product_category,
                               product_price="25.00",
                               product_stock=12,
                               slug=slugify("Fine Stripe Long Sleeve Shirt, Green"))
        response = self.client.get(reverse('product-list',
                                           kwargs={'slug': 'mens-formalwear'}))
        self.assertEqual(len(response.context['object_list']), 3)


class ProductTestCase(TestCase):
    """Test case for products"""
    def setUp(self):
        self.client = Client()
        ProductCategory.objects.create(category_name="Men's Shoeware",
                                       slug=slugify("Men's Shoeware"))
        ProductCategory.objects.create(category_name="Men's Casualwear",
                                       slug=slugify("Men's Casualwear"))
        ProductCategory.objects.create(category_name="Women's Formalwear",
                                       slug=slugify("Women's Formalwear"))

    def test_product_detail_view(self):
        """Test if a product detail view is properly accessible after
        product creation
        """
        product_category = ProductCategory.objects.get(category_name="Men's Shoeware")
        test_product = Product.objects.create(product_name="Fine Stripe Short Sleeve Shirt, Green",
                                              product_category=product_category,
                                              product_price="34.00",
                                              product_stock=12,
                                              slug=slugify("Fine Stripe Short Sleeve Shirt, Green"))
        response = self.client.get(reverse('product-detail',
                                           kwargs={'category_slug': "mens-shoeware",
                                                   'slug': 'fine-stripe-short-sleeve-shirt-green'}))
        self.assertEqual(response.status_code, 200)
