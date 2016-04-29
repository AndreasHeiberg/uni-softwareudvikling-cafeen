from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^product-groups$', views.product_groups, name='product_groups'),
    url(r'^product-groups/([0-9]+)$', views.product_group, name='product_group'),
    url(r'^products$', views.products, name='products'),
    url(r'^products/([0-9]+)$', views.product, name='product')
]
