from django.urls import path
from . import views
from django.shortcuts import render, redirect

urlpatterns = [
    path('',views.home, name = 'home'),
    path('task_list',views.task_list, name = 'task_list'),
    path('2',views.history, name = 'history'),
    path('3',views.contact, name = 'contact'),
    path('display/<int:ab>',views.display, name = 'display'),
    path('edit/<int:pk>',views.edit, name = 'edit'),
    path('delete/<int:ak>',views.delete, name = 'delete'),
]