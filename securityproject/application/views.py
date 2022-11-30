from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Order
import sqlite3


@login_required
def sendorderView(request):
    if request.method == 'POST':
        name = request.POST.get('order_name')
        price = request.POST.get('price')
        date = timezone.now()
        status = 'Pending'
        customer = User.objects.get(username = request.POST.get('customer'))
        try:
             Order.objects.create(name = name, price = price, date_created = date, status = status, customer = customer)
        except:
            pass

    return redirect('/')

@login_required
def setdeliveredView(request):

    name = request.POST.get('name')
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE application_order SET status = 'Delivered' WHERE name = '%s';" % (name,))
        connection.commit()
    except:
        pass
     
    return redirect('/')

'''@login_required
def setdeliveredView(request):
    
    if request.method == 'POST':

        orderid = request.POST.get('id')
        order = Order.objects.filter(id = orderid).first()
        user = request.user

        if order.customer == user:

            order.status = 'Delivered'
            order.save()

    return redirect('/')'''


@login_required
def deleteorderView(request, orderid):
    
    Order.objects.filter(id = orderid).delete()

    return redirect('/')

# Create your views here.
@login_required
def indexView(request):
    orders = Order.objects.filter(customer = request.user)
    return render(request, 'application/index.html', {'orders': orders})


