from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('',views.Grand,name='help'),
    path('Form',views.Free,name='do'),
]