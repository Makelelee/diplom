from django.contrib import admin
from main.models import User, Category, Product
# Register your models here.


class AdminUser(admin.ModelAdmin):
    pass


class AdminCategory(admin.ModelAdmin):
    search_fields = ('name',)


class AdminProduct(admin.ModelAdmin):
    search_fields = ('name', 'category__name')


admin.site.register(User, AdminUser)
admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
