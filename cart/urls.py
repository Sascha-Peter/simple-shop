from django.conf.urls import url

urlpatterns = [
    url(r'^add/(?P<product_id>\d+)/(?P<quantity>\d+)/',
        'cart.views.add_to_cart', name="cart-add"),
    url(r'^remove/(?P<product_id>\d+)/',
        'cart.views.remove_from_cart', name="cart-remove"),
    url(r'^show/',
        'cart.views.get_cart', name="cart-show"),
]
