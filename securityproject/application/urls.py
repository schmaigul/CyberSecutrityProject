from django.urls import path

from .views import indexView, sendorderView, setdeliveredView, deleteorderView

urlpatterns = [
    path("", indexView, name='index'),
    path("setdelivered/", setdeliveredView, name = "setdelivered"),
    path("sendorder/", sendorderView, name = "sendorder"),
    path("deleteorder/<int:orderid>", deleteorderView, name = "deleteorder")
]