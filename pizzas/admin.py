from django.contrib import admin

# Register your models here.
'''注册模块'''
from pizzas.models import Pizza , Topping
admin.site.register(Pizza)
admin.site.register(Topping)