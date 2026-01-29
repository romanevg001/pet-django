from django.contrib import admin
from django.urls import path
# from .views import shop_index, groups_list, products_list, orders_list, create_product
from .views import (
    ShopIndexView,
    GroupsListView,
    ProductDetailView,
    ProductListView,
    OrderListView,
    ProductCreateView,
    OrderDetailsView,
    ProductUpdateView,
    ProductDeleteView
)

app_name="shopapp"

urlpatterns = [
    # path('', shop_index, name="index"),
    # path('groups/', groups_list, name="groups_list"),
    # path('products/', products_list, name="products_list"),
    # path('orders/', orders_list, name="orders_list"),
    # path('products/create', create_product, name="create_product"),

    path('', ShopIndexView.as_view(), name="index"),
    path('groups/', GroupsListView.as_view(), name="groups_list"),
    path('products/', ProductListView.as_view(), name="products_list"),
    path('products/create', ProductCreateView.as_view(), name="create_product"),
    path('products/<int:pk>', ProductDetailView.as_view(), name="product_details"),
    path('products/<int:pk>/update', ProductUpdateView.as_view(), name="product_update"),
    path('products/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete"),

    path('orders/', OrderListView.as_view(), name="orders_list"),
    path('orders/<int:pk>', OrderDetailsView.as_view(), name="order_details"),

]
