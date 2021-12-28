from core.helpers.cotacoes import CotacaoMoedas
from core.models import Cotacao
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from core.forms import CotacaoModelForm
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def site(request):
    return render(request, 'core/index.html')


class CotacaoHtmxCreateView(SuccessMessageMixin, CreateView):
    model = Cotacao
    template_name = 'core/partials/htmx_cotacao_dados.html'
    form_class = CotacaoModelForm
    success_message = 'Cotação concluída!'

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        moeda = self.request.POST['moeda']

        data_inicial = datetime.strptime(
            self.request.POST['data_inicial'], '%Y-%m-%d').date()
        data_final = datetime.strptime(
            self.request.POST['data_final'], '%Y-%m-%d').date()

        CotacaoMoedas(moeda, data_inicial, data_final).atualizar_banco()

        response['HX-Trigger'] = 'hx-list-updated'
        messages.success(self.request, self.get_success_message())
        return response


class CotacaoHtmxListView(ListView):
    model = Cotacao
    template_name = 'core/partials/htmx_cotacao_list.html'
    context_object_name = 'cotacoes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cotacoes"] = Cotacao.objects.all().order_by('-id')
        return context
