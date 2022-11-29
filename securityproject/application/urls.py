from django.urls import path

from .views import indexView, sendorderView, setdeliveredView, deleteorderView

urlpatterns = [
    path("", indexView, name='index'),
    path("setdelivered/<int:orderid>", setdeliveredView, name = "setdelivered"),
    path("sendorder/", sendorderView, name = "sendorder"),
    path("deleteorder/", deleteorderView, name = "deleteorder")
]