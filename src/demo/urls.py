from django.urls import path

from . import views

urlpatterns = [
    # login
    path('', views.index, name='index'),

    # top
    path('', views.top, name='top'),
]
