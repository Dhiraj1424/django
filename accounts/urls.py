from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home, name="home"),
    path('products/',views.products, name="products"),
    path('customer/<str:pk_test>/',views.customer, name="customer"),
    path('navbar/',views.navbar),
    # path('create_order/',views.createOrder,name="create_order"),

    path('create_order/<str:pk>',views.createOrder,name="create_order"),
    
    path('update_Order/<str:pk>',views.updateOrder,name="update_Order"),
    path('delete_Order/<str:pk>',views.deleteOrder,name="delete_Order"),


]
