
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from home.views import change_lang

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
]

urlpatterns=[
    *i18n_patterns(*urlpatterns,prefix_default_language=False),
    path('<str:lang>/',change_lang,name='change_lang'),

]