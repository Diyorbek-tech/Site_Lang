from django.contrib import admin
from .models import Product
from modeltranslation.admin import TranslationAdmin

# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('title',)
