from django.contrib import admin
from .models import Category, Page, UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',]

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'category')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'website', 'picture', 'email']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
