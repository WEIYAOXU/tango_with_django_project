from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    llist_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page)


# Register your models here.
