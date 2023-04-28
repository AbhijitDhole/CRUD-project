from django.urls import path
from . import views

urlpatterns = [
    path('reg/', views.signUpView, name= "signup_url"),
    path('log/', views.loginView, name ="login_url"),
    path('lot/', views.logoutView, name='logout_url')
]
