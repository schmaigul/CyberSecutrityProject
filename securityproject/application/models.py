from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
    )
    name = models.CharField(max_length = 50)
    price = models.IntegerField()
    date_created = models.DateTimeField()
    status = models.CharField(max_length = 50, choices=STATUS_CHOICES)

    customer = models.ForeignKey(User, on_delete = models.CASCADE)
