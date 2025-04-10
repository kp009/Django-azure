from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),  # Root URL for 'hello_world' view
]
