# Register your models here.
from django.contrib import admin

from .models import User
from .models import Category
from .models import Item

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Item)
