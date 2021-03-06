from django.contrib import admin
from .models import Country, Cart, CartItem, Order
# Register your models here.

admin.site.register(Country)
admin.site.register(CartItem)
admin.site.register(Cart)


@admin.register(Order)
class QuestionAdmin(admin.ModelAdmin):
   list_display = ['first_name', 'last_name', 'items', 'total', 'phone', 'address','date', 'comment']

