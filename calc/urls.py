from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Add', views.add, name='Add')
]