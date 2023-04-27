from django.urls import path
from . import views


app_name = 'app_quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
]