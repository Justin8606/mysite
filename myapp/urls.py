from django.urls import path,include
from myapp.views import index
from .views import news_one

urlpatterns = [
    path('',index),
    path('new',news_one)
]



