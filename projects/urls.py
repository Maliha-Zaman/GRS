from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name='home'),
    path('verify/<str:verification_token>/', views.verify_email, name='verify_email'),
    path('password_reset/', views.password_reset_request, name='password_reset_request'),
    path('reset/<str:token>/', views.password_reset, name='password_reset'),
    # path('start_backend/', views.start_backend, name='start_backend'),
    path('start_backend/', views.start_backend, name='start_backend'),
    path('moving/', views.moving, name='moving'),
    # path('audio/', views.audio, name='audio'),
    
    path('start_backendMultiple/', views.start_backendMultiple, name='start_backendMultiple'),
    path('gestureTest/', views.gestureTest, name='gestureTest'),
     path('features/', views.features, name='features'),
    path('test/', views.test, name='test'),
    # path('gestures/', views.gestures_view, name='gestures'),
    path('gestures/', views.gestures, name='gestures'),
]
