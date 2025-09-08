from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_project, name='order_project'),
]