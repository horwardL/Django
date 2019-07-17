from django.urls import path

from . import views

urlpatterns = [
    # if user go to url '' follow by it,
    # then goto views.py and call index function
    path('', views.index, name='index'),
]
