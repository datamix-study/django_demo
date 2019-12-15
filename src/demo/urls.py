from django.urls import path
from . import views

app_name = 'demo'
urlpatterns = [

    # index
    path('', views.index, name='index'),

    # login
    path('login', views.login, name='login'),

    # login
    path('logout', views.logout, name='logout'),

    # top
    path('top', views.top, name='top'),

    # 商品一覧/検索
    path('list', views.List.as_view(), name='list'),

    # 商品詳細
    path('detail/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),

    # 商品詳細からのカートへの追加
    path('item/add/', views.item_add, name='item_add'),

    # カート
    path('cart', views.cart, name='cart'),
]
