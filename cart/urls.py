from django.conf.urls import url
from cart.views import add_to_cart, remove_from_cart, get_cart

urlpatterns = [
    url(r'^add/(?P<product_id>\d+)/(?P<quantity>\d+)/',
        add_to_cart, name="cart-add"),
    url(r'^remove/(?P<product_id>\d+)/',
        remove_from_cart, name="cart-remove"),
    url(r'^show/',
        get_cart, name="cart-show"),
]
