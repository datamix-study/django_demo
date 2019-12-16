from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView

from .models import User, Item, Cart, CartItem


def index(request):
    return render(request, 'demo/login.html')


def login(request):
    try:
        # formを経由する
        user = User.objects.get(username=request.POST['username'], password=request.POST['password'])

        cart = None
        try:
            cart = Cart.objects.filter(user_id=user.pk, del_flg=False)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user_id=user.pk)
            cart.save()

        request.session['cart'] = serializers.serialize('json', Cart.objects.all())
        request.session['username'] = user.username
        return redirect('demo:list')

    except User.DoesNotExist:
        context = {"message": "User DoesNotExist"}
        return render(request, 'demo/login.html', context)

    except User.MultipleObjectsReturned:
        context = {"message": "Multiple User found"}
        return render(request, 'demo/login.html', context)


def logout(request):
    request.session.flush()
    return redirect('demo:index')


class List(generic.ListView, LoginRequiredMixin):
    model = Item
    context_object_name = 'item_list'
    paginate_by = 10
    template_name = 'demo/list.html'

    def get_queryset(self):
        keyword = self.request.GET.get('keyword', '')
        if keyword:
            return Item.objects.filter(name__contains=keyword)
        else:
            return Item.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['keyword'] = self.request.GET.get('keyword', '')
        return context


class ItemDetailView(DetailView):
    item = Item

    def get_object(self):
        return Item.objects.get(pk=self.kwargs["pk"])


def item_add(request):
    # TODO:formを経由する

    # login確認
    if not "username" in request.session:
        # セッションの中身を全て削除した上でlogin画面へ遷移
        return redirect('demo:logout')

    # 競合状態、在庫数を考慮してカートへ商品追加

    # 元のページへ遷移
    return redirect(request.META['HTTP_REFERER'])


def cart(request):
    return render(request, 'demo/cart.html')
