from django.urls import path
from . import views

urlpatterns = [
    path('send/', views.send, name='send'),
    path('list_message/', views.list_message, name='list_message'),
]
