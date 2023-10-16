from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name='home'),
    path('verify/<str:verification_token>/', views.verify_email, name='verify_email'),
    path('start_backend/', views.start_backend, name='start_backend'),
   
]
