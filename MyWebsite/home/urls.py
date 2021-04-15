#crate by mrinmoy
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name = "home"),
    path('user/', views.userPage, name="user-page"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('about', views.about),
    path('contact', views.contact),
    path('services', views.services, name= "products"),
    path('dashboard', views.dashboard, name = "dashboard"),
    path('customer/<str:pk_test>/', views.customer, name = "customer"),
    path('create_order/', views.createOrder, name = "create_order"),
    path('create_products/', views.createProducts, name = "create_products"),
    path('update_order/<str:pk>/', views.updateOrder, name = "update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name = "delete_order"),
    path('create_customer/', views.createCustomer, name = "create_customer"),
    path('update_customer/<str:pk_2>/', views.updateCustomer, name="update_customer"),
    path('account/', views.accountSettings, name="account"),
    # path('delete_customer/<str:pk>/', views.deleteCustomer, name="delete_customer"),


]
