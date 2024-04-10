from django.contrib import admin
from .models import MenuItem

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1

@admin.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    inlines = (MenuItemInline,)
