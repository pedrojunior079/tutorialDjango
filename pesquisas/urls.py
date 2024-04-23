from django.urls import path

from . import views

app_name = "pesquisas"

urlpatterns = [
  path("", views.index, name="index"),
  path("<int:pergunta_id>/", views.detalhe, name="detalhe"),
  path("<int:pergunta_id>/resultados/", views.resultados, name="resultados"),
  path("<int:pergunta_id>/voto/", views.voto, name="voto"),
]

