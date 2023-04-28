from django.urls import path
from . import views

urlpatterns = [
    path('ad/', views.addOrderView, name= 'addorder_url'),
    path('sh/', views.showOrderView, name = 'showorder_url'),
    path('up/<int:pk>/', views.updateOrderView, name='updateorder_url'),
    path('dl/<int:pk>/', views.deleteOrderView, name= 'deleteorder_url')
    
]
