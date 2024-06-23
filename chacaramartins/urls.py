from django.urls import path
from chacaramartins.views import index

urlpatterns = [
    path('', index)
]