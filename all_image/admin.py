from django.contrib import admin

from .models import *
# Register your models here.

# admin.site.register(AllImage)

@admin.register(AllImage)
class AllImageAdmin(admin.ModelAdmin):
	exclude = ("idx",)
