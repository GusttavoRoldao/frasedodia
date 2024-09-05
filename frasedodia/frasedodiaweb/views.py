from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, "frasedodiaweb/index.html")

def atualiza_texto(request): 
    novo_texto = "Atualizacao deu certo" #request.GET.get('novo_texto', 'Texto padrão do servidor!')
    return JsonResponse({'novo_texto': novo_texto})