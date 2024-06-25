from django.shortcuts import render


def index(request):
    return render(request, 'chacaramartins/index.html')

def galeria(request):
    return render(request, 'chacaramartins/galeria.html')

def localizacao(request):
    return render(request, 'chacaramartins/localizacao.html')