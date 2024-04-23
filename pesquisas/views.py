from django.shortcuts import render
from django.http import HttpResponse
from .models import Pergunta
from django.shortcuts import get_object_or_404


def index(request):
    latest_pergunta_list = Pergunta.objects.order_by("-pub_data")[:5]
    context = {"latest_pergunta_list": latest_pergunta_list}
    return render(request, "pesquisas/index.html", context)

def detalhe(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, "pesquisas/detalhe.html", {"pergunta": pergunta})
    

def resultados(request, pergunta_id):
    response = "Você está vendo os resultados da pergunta %s."
    return HttpResponse(response % pergunta_id)

def voto(request, pergunta_id):
    return HttpResponse("Você está votando na questão %s." % pergunta_id)






