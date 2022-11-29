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

        Order.objects.create(name = name, price = price, date_created = date, status = status, customer = customer)

    return redirect('/')

@login_required
def setdeliveredView(request, orderid):

    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE application_order SET status = 'Delivered' WHERE id = %s;" % (orderid))
        connection.commit()
    except:
        pass
     
    return redirect('/')

@login_required
def deleteorderView(request):
    
    Order.objects.filter(id = request.POST.get('id')).delete()

    return redirect('/')

# Create your views here.
@login_required
def indexView(request):
    orders = Order.objects.filter(customer = request.user)
    return render(request, 'application/index.html', {'orders': orders})


