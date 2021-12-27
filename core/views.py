from django.shortcuts import render
from django.views.generic import CreateView, ListView
from core.forms import CotacaoModelForm
from django.http import JsonResponse

from core.models import Cotacao

from core.helpers.cotacoes import CotacaoMoedas


def site(request):
    return render(request, 'core/index.html')


class CotacaoHtmxCreateView(CreateView):
    model = Cotacao
    template_name = 'core/partials/htmx_cotacao_dados.html'
    form_class = CotacaoModelForm


class CotacaoHtmxListView(ListView):
    model = Cotacao
    template_name = 'core/partials/htmx_cotacao_list.html'
    context_object_name = 'cotacoes'


# def atualizar_valor_indexador(request):
#     cotacao = str(CotacaoMoedas(
#         request.POST['moeda'], request.POST['data']).obter_cotacao()).replace('.', ',')

#     return JsonResponse({'cotacao': cotacao}, safe=False)
