from django.shortcuts import render
from django.views.generic import CreateView, ListView
from core.forms import CotacaoModelForm
from datetime import datetime, timedelta
from django.urls import reverse_lazy


from core.models import Cotacao

from core.helpers.cotacoes import CotacaoMoedas


def site(request):
    return render(request, 'core/index.html')


class CotacaoHtmxCreateView(CreateView):
    model = Cotacao
    template_name = 'core/partials/htmx_cotacao_dados.html'
    form_class = CotacaoModelForm
    success_message = 'Cotação concluida'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        context = super().post(request, *args, **kwargs)
        moeda = self.request.POST['moeda']

        data_inicial = datetime.strptime(
            self.request.POST['data_inicial'], '%Y-%m-%d').date()
        data_final = datetime.strptime(
            self.request.POST['data_final'], '%Y-%m-%d').date()

        while data_inicial <= data_final:
            CotacaoMoedas(moeda, data_inicial, data_final).atualizar_banco()
            data_inicial += timedelta(days=1)

        context['HX-Trigger'] = 'hx-list-updated'

        return context

    def get_success_url(self):
        return reverse_lazy('core:index')


class CotacaoHtmxListView(ListView):
    model = Cotacao
    template_name = 'core/partials/htmx_cotacao_list.html'
    context_object_name = 'cotacoes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cotacoes"] = Cotacao.objects.all().order_by('-id')
        return context
