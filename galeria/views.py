
from django.shortcuts import render


# Guarda a onde as requisições vão ser chamadas --> templetes/html

def index (request):
    dados = {
    1: {"nome" : "nebulosa de carina",
        "legenda" : "webbtelecope.org / NASA / ames webb"},
    2: {"nome" : "Galaxia NGC 1079",
        "legenda" : "nasa.org / NASA / Huble" }
}
    
    return render(request, 'galeria/index.html', {"cards" : dados}) # enviando os dados dos cards junto com o render 

def imagem (request):
    return render(request, 'galeria/imagem.html') 