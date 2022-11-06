from django.urls import path,include
from .views import register

urlpatterns = [
    
    path('register/',register,name='register'),
#     path('products/<int:id>',product_details,name='product_details'),
#     path('products/add',add_product,name='add_product'),
#     path('products/update/<int:id>',update_product,name='update_product'),
#     path('products/delete/<int:id>',delete_product,name='delete_product')
 ] 