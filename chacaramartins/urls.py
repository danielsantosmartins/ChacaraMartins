from django.urls import path
from chacaramartins.views import index, galeria, localizacao

urlpatterns = [
    path('', index, name='inicio'),
    path('galeria/', galeria, name='galeria'),
    path('localizacao/', localizacao, name='localizacao')
]