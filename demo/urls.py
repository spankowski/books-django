from django.urls import path
from . import views

urlpatterns = [
    path('first', views.first ),
    path('abc', views.abc ),
]
