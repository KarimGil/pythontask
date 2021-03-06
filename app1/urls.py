from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('employee_list', views.employee, name='employee_list'),
    path('logout', views.logout, name='logout')
]