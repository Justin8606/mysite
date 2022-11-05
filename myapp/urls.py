from django.urls import path,include
from myapp.views import index
from .views import news_one, product_details,products,add_product,update_product,delete_product

urlpatterns = [
    path('',index),
    path('new/',news_one),
    path('products/',products,name='products'),
    path('products/<int:id>',product_details,name='product_details'),
    path('products/add',add_product,name='add_product'),
    path('products/update/<int:id>',update_product,name='update_product'),
    path('products/delete/<int:id>',delete_product,name='delete_product')
]



