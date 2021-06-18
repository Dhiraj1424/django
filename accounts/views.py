from django.db.models import query
from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm

# Create your views here.
# yo chali inline formset ko lagi

from django.forms import inlineformset_factory

# import filter
from.filters import *


def home(request):
    order = Order.objects.all()
    customer = Customer.objects.all()

    total_order = order.count()
    total_customer = customer.count()
    deliver = order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()
    context = {'order': order,
               'customer': customer,
               'total_order': total_order,
               'pending': pending,
               'deliver': deliver

               }
    return render(request, 'accounts/dashboard.html', context)


def products(request):
    product = Product.objects.all()
    return render(request, 'accounts/products.html', context={'product': product})


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
#query all the order
    orders = customer.order_set.all()
    order_count = orders.count()
    # query order and through in  filter base on what request data is we filter on down we 
    #have request.get 
    myFilter=OrderFilter(request.GET,queryset=orders)
    orders=myFilter.qs


    context = {'customer': customer,
               'orders': orders, 'order_count': order_count,
               'myFilter':myFilter}
    return render(request, 'accounts/customer.html', context)


def navbar(request):
    return render(request, 'accounts/navbar.html')


# def createOrder(request):
#     # orderform chai forms.py ma xa ra yes lai mathi import garna parxa

#     form = OrderForm()
#     if request.method == 'POST':
#         # print('pricing post',request.POST)
#         # Create a form instance from POST data.

#         # request.POST le new item create garxa
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form': form}
#     return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    # id =pk kina rakehoko vane id ma handa tesko detailts sabai aaus
    # order vanne model ko sabbi field ko value haru get garue
    order = Order.objects.get(id=pk)
    # ra instace=order garda yesle fileld hare pre fielld garxa
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'item': order
    }
    return render(request, 'accounts/delete.html', context)


# def creatOrder(request, pk):
#     # Customer is parent and child is order aand product and status are fields of child
#     # we allowed
#     OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
#     customer = Customer.objects.get(id=pk)
#     formset = OrderFormSet(instance=customer)
#     # initial rakda form a dictionary ma j pass gareko xau tyo dekhau xaa
#     # inital is a instance
#     # form=OrderForm(initial={'customer':customer})

#     if request.method == 'POST':
#         # form=OrderForm(request.POST)
#         formset = OrderFormSet(request.POST, instance=customer)

#         if formset.is_valid():
#             formset.save()
#             return redirect('/')

#     context = {'formset': formset}
#     return render(request, 'accounts/order_form.html', context)



def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	#form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
		#print('Printing POST:', request.POST)
		#form = OrderForm(request.POST)
	    formset = OrderFormSet(request.POST, instance=customer)
	    if formset.is_valid():
		    formset.save()
		    return redirect('/')

    context = {'form':formset}
    return render(request, 'accounts/order_form.html', context)
