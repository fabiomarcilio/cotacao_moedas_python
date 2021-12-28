from django.shortcuts import render
from django.views.generic import CreateView, ListView
from core.forms import CotacaoModelForm
from django.http import JsonResponse
from datetime import datetime, timedelta


from core.models import Cotacao

from core.helpers.cotacoes import CotacaoMoedas


def site(request):
    return render(request, 'core/index.html')


class CotacaoHtmxCreateView(CreateView):
    model = Cotacao
    template_name = 'core/partials/htmx_cotacao_dados.html'
    form_class = CotacaoModelForm

    def post(self, request, *args, **kwargs):
        context = super().post(request, *args, **kwargs)
        moeda = self.request.POST['moeda']

        data_inicial = datetime.strptime(
            self.request.POST['data_inicial'], '%Y-%m-%d').date()
        data_final = datetime.strptime(
            self.request.POST['data_final'], '%Y-%m-%d').date()

        while data_inicial <= data_final:
            CotacaoMoedas(moeda, data_inicial).atualizar_banco()
            data_inicial += timedelta(days=1)
        return context


class CotacaoHtmxListView(ListView):
    model = Cotacao
    template_name = 'core/partials/htmx_cotacao_list.html'
    context_object_name = 'cotacoes'
