from django.contrib import admin
from .models import Category, Page
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    pass


class PageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
