from django.urls import path
from . import views

urlpatterns = [
    path("", views.tests, name = "test"),
    path("create_order/", views.createOrder, name="create_order")
]
