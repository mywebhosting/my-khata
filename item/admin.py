from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	exclude = ('idx',)
	# fields = ('product_id','product_name','product_qty_type','product_qty','product_price','status') # Working

# admin.site.register(Product)
admin.site.register(ProductQtyType)
