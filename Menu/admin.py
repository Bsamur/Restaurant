from django.contrib import admin
from .models import *
# Register your models here.

class ShopperAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_now', 'date_now', 'total',)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'offer', 'category', 'slug',)
    list_editable = ('price', 'is_active', 'offer', )
    readonly_fields = ('slug',)

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Shopper,ShopperAdmin)
admin.site.register(Cari)
admin.site.register(Daire)