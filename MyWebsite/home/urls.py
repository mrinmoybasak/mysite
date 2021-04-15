#crate by mrinmoy
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
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

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
         name="password_reset_complete"),

]
