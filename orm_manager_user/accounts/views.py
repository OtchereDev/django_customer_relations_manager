from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm,CreateUserForm
from django.contrib.auth.decorators import login_required
from .filter import PermissionFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.views.generic import CreateView

from .forms import UserSignUpForm,StaffSignUpForm

from .decorators import staff_required


class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'account/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'User'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')

# def registerPage(request):
#     if request.user.is_authenticate:
#         return redirect('home')
    
#     form =CreateUserForm()

#     if request.method=='POST':
#         form=CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request,'Account was created for '+user)
#             return redirect('login')


#     context={
#         'form':form
#     }
#     return render(request,'account/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or password is incorrect')
    context={

    }
    return render(request, 'account/login.html',context)
from django.contrib.auth import get_user_model

def logoutUser(request):
    
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@staff_required
def dashboard(request):
    orders=Permission.objects.all()
    customer=Permission.objects.all()
    total_customers=customer.count()
    total_orders=orders.count()
    pending=orders.filter(status='Pending').count()
    context={
        'orders':orders,
        'customers':customer,
        'total_customers':total_customers,
        'total_orders':total_orders,
    
        'pending':pending,
    }
    return render(request,'account/dashboard.html',context)

@login_required(login_url='login')
def home(request):
    products=Product.objects.all()
    permissions=Permission.objects.filter(customer=request.user)
    
    context={
        'products':products,
        'permissions':permissions
    }
    return render(request,'account/products.html',context)

@login_required(login_url='login')
@staff_required
def customer(request,pk):
    customer=Customer.objects.get(id=pk)

    orders=customer.permission_set.all()
    orders_count=orders.count()

    myFilter=PermissionFilter(request.GET,queryset=orders)
    orders=myFilter.qs


    context={
        'myFilter':myFilter,
        'customer':customer,
        'orders':orders,
        'orders_count':orders_count,
    }

    return render(request,'account/customer.html',context)

@login_required(login_url='login')
def createOrder(request):

    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    content={
        'form':form
    }
    return render(request, 'account/order_form.html',content)

@login_required(login_url='login')
@staff_required
def updateOrder(request,pk):
    order=Permission.objects.get(id=pk) 
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    content={
        'form':form
    }
    return render(request, 'account/order_form.html',content)

@login_required(login_url='login')
@staff_required
def deleteOrder(request,pk):
    order=Permission.objects.get(id=pk) 
    if request.method=='POST':
        order.delete()
        return redirect('/')
    context={'item':order,}
    return render(request,'account/delete.html',context)


class StaffSignUpView(CreateView):
    
    model = User
    form_class = StaffSignUpForm
    template_name = 'account/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'staff'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


def requestPermission(request,pk):
    user=request.user
    product=Product.objects.get(id=pk)
    requests=Permission.objects.create(customer=user,product=product,status='Pending')
    requests.save()
    return redirect('home')

def acceptPermission(request,pk):
    requests=Permission.objects.get(id=pk)
    requests.status='Accepted'
    requests.save()
    return redirect('dashboard')

def deniedPermission(request,pk):
    requests=Permission.objects.get(id=pk)
    requests.status='Denied'
    requests.save()
    return redirect('dashboard')