from django.conf.urls import url
from .views import ProductCategoryList, ProductDetailView

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', ProductCategoryList.as_view(),
        name="product-list"),
    url(r'^(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/', ProductDetailView.as_view(),
        name="product-detail"),
]
