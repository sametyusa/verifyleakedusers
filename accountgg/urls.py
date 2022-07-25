from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginView, name='loginView'),
    path('check', views.index, name='index'),
    path('logout',views.logOutView,name='logOutView')
]