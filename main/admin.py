from django.contrib import admin

from main.models import Product, Category

# Register your models here.

#admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'category', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'category')


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
