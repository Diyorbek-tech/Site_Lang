from .models import Product
from modeltranslation.translator import TranslationOptions,register

@register(Product)
class Producttranslation(TranslationOptions):
    fields=('title','description')
