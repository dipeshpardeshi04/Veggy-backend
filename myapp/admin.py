from django.contrib import admin

# Register your models here.
from .models import User,Products,Cart,CartItem,Student
# admin.site.register(User)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Student)