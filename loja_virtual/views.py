from django.shortcuts import render

from django.shortcuts import render

def imagens(request):
    return render(request, 'imagens.html')

def preços(request):
    return render(request, 'preços.html')

def descrição(request):
    return render(request, 'descrição.html')

