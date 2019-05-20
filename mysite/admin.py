from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku','name','price','qty','size','pub_date','edit_date')     # 设置要显示的字段
    search_fields = ('sku','name','price','qty','size')                 #开启搜索功能，设置搜索字段
admin.site.register(Product,ProductAdmin)