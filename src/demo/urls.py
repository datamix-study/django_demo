from django.urls import path

from . import views

app_name = 'demo'
urlpatterns = [
    # index
    path('', views.index, name='index'),

    # login
    path('login', views.login, name='login'),

    # top
    path('top', views.top, name='top'),
]
