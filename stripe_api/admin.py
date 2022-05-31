from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name', 'price']
    list_display = ['id', 'name', 'price', 'description']

