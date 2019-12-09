from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView

from .models import User, Item, Cart, CartItem


def index(request):
    return render(request, 'demo/login.html')


def login(request):
    try:
        user = User.objects.get(username=request.POST['username'], password=request.POST['password'])

        # TODO:cartオブジェクトの削除（動作確認を簡易にする為、ログイン時にカートへ商品を投入）
        cart = None
        try:
            cart = Cart.objects.get(user_id=user.pk)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user_id=user.pk)
            cart.save()

            item = Item.objects.get(pk=1)
            cart_item = CartItem.objects.create(item=item, cart=cart)
            cart_item.quantity += 1
            cart_item.save()

        request.session['cart'] = serializers.serialize('json', Cart.objects.all())
        request.session['username'] = user.username
        return HttpResponseRedirect(reverse('demo:list'))

    except User.DoesNotExist:
        context = {"message": "User DoesNotExist"}
        return render(request, 'demo/login.html', context)

    except User.MultipleObjectsReturned:
        context = {"message": "Multiple User found"}
        return render(request, 'demo/login.html', context)


def top(request):
    return render(request, 'demo/top.html')


class List(generic.ListView, LoginRequiredMixin):
    model = Item
    context_object_name = 'item_list'
    paginate_by = 10
    template_name = 'demo/list.html'

    def get_queryset(self):
        return Item.objects.all()


class ItemDetailView(DetailView):
    item = Item

    def get_object(self):
        return Item.objects.get(pk=1)


def cart(request):
    return render(request, 'demo/cart.html')
