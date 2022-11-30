from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Order
import sqlite3


'''import logging
logger = logging.getLogger(__name__)'''

@login_required
def sendorderView(request):
    if request.method == 'POST':
        name = request.POST.get('order_name')
        price = request.POST.get('price')
        date = timezone.now()
        status = 'Pending'
        customer = User.objects.get(username = request.POST.get('customer'))
        order = Order.objects.create(name = name, price = price, date_created = date, status = status, customer = customer)
        #logger.info(f"A new order was made with the id {order.id}")

    return redirect('/')

'''@login_required
def sendorderView(request):
    if request.method == 'POST':
        name = request.POST.get('order_name')
        price = request.POST.get('price')
        date = timezone.now()
        status = 'Pending'
        try:
            customer = User.objects.get(username = request.POST.get('customer'))
            Order.objects.create(name = name, price = price, date_created = date, status = status, customer = customer)
        except ValueError():
            logger.warning("Invalid values inserted")

    return redirect('/')'''

@login_required
def setdeliveredView(request):

    name = request.POST.get('name')
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE application_order SET status = 'Delivered' WHERE name = '%s';" % (name,))
        connection.commit()
    except:
        #logger.warning('Platform is running at risk')
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

'''
@login_required
def deleteorderView(request, orderid):
    if request.method == 'POST':

        user = request.user
        order = Order.objects.filter(id = orderid).first()

        if order.customer == user:

            order.delete()

    return redirect('/')
'''

# Create your views here.
@login_required
def indexView(request):
    orders = Order.objects.filter(customer = request.user)
    return render(request, 'application/index.html', {'orders': orders})


