from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import OrderFrom, ProductsFrom, CustomerForm, CreateUserForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'index.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def dashboard(request):

    orders = Order.objects.all()

    customers= Customer.objects.all()

    total_customers = customers.count()


    context = {'orders': orders, 'customers':customers,  'total_customers': total_customers}
    return render(request,'dashboard.html', context)


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

@login_required(login_url='login')
def services(request):
    products = Product.objects.all()
    return render(request,'services.html', {'products': products})

@login_required(login_url='login')
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()
    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders':orders,'order_count':order_count ,'myFilter':myFilter }
    return render(request,'customer.html', context)

@login_required(login_url='login')
def createOrder(request):
    form = OrderFrom()
    if request.method == 'POST':
         #print('Printing POST:', request.POST)
         form = OrderFrom(request.POST)
         if form.is_valid():
             form.save()
             return redirect('/dashboard')


    context = {'form': form}
    return render(request, 'order_form.html', context)

@login_required(login_url='login')
def createProducts(request):
    form = ProductsFrom()
    if request.method == 'POST':
         #print('Printing POST:', request.POST)
         form = ProductsFrom(request.POST)
         if form.is_valid():
             form.save()
             return redirect('/dashboard')

    context = {'form': form}
    return render(request, 'order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderFrom(instance=order)

    if request.method == 'POST':
        form = OrderFrom(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    context = {'form':form}
    return render(request,'order_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/dashboard')
    context = {'item':order}
    return render(request, 'delete.html', context)


@login_required(login_url='login')
def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    context = {'form': form}

    return render(request, 'customer_form.html', context )


@login_required(login_url='login')
def updateCustomer(request, pk_2):
    customer = Customer.objects.get(id=pk_2)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')

    context = {'form': form, 'customer': customer}
    return render(request, 'order_form.html', context)
