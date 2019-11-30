from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView

from .models import User, Item


def index(request):
    return render(request, 'demo/login.html')


def login(request):
    try:
        user = User.objects.get(username=request.POST['username'], password=request.POST['password'])
        # print(request.POST['username'])
        # print(request.POST['password'])
        # user = User.objects.get(pk=1)

        request.session['username'] = user.username
        return render(request, 'demo/list.html')

    except User.DoesNotExist:
        context = {"message": "User DoesNotExist"}
        return render(request, 'demo/login.html', context)

    except User.MultipleObjectsReturned:
        context = {"message": "Multiple User found"}
        return render(request, 'demo/login.html', context)


def top(request):
    return render(request, 'demo/top.html')


class List(generic.ListView, LoginRequiredMixin):
    # TODO: 仮置のためDB定義後に修正する
    class Item:
        def __init__(self, _id, _name, _description):
            self.id = _id
            self.name = _name
            self.description = _description
            self.img_src = 'https://avatars3.githubusercontent.com/u/56213093?s=200&v=4'

    model = Item
    context_object_name = 'item_list'
    paginate_by = 10
    template_name = 'demo/list.html'

    def get_queryset(self):
        return [self.Item(i, '商品{}'.format(i), '商品概要{}'.format(i)) for i in range(25)]


class ItemDetailView(DetailView):
    item = Item

    def get_object(self):
        return Item.objects.get(pk=1)