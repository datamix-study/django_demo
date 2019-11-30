from django.urls import path
from . import views

app_name = 'demo'
urlpatterns = [

    # index
    path('', views.index, name='index'),

    # login
    path('login', views.login, name='login'),

    # 商品一覧
    path('top', views.top, name='top'),

    # 商品詳細
    path('detail/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
]
