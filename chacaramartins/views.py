from django.shortcuts import render
from chacaramartins.models import Fotografia

def index(request):
    return render(request, 'chacaramartins/index.html')

def galeria(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'chacaramartins/galeria.html', {"cards": fotografias})

def localizacao(request):
    return render(request, 'chacaramartins/localizacao.html')