from django.shortcuts import render
from .models import Product
# Create your views here.

from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation


def indexview(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, 'index.html', context)


def change_lang(request, lang):
    for language, _ in settings.LANGUAGES:
        translation.activate(language)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(lang)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        responce = HttpResponseRedirect(next_url)
        responce.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang)
    else:
        responce = HttpResponseRedirect('/')

    return responce
