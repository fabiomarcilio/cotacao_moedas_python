from django.views.generic.base import TemplateView
from core.helpers.cotacoes import CotacaoMoedas
from core.models import Cotacao
from datetime import datetime, timedelta
from core.forms import CotacaoModelForm
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
import json
from core.helpers.funcoes import retornar_valores_grafico, retornar_moeda, retornar_data_inicial, verifica_dia_util


class SiteTemplateview(TemplateView):
    template_name = 'core/index.html'


class CotacaoHtmxCreateView(SuccessMessageMixin, CreateView):
    model = Cotacao
    template_name = 'core/partials/htmx_cotacao_dados.html'
    form_class = CotacaoModelForm

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        moeda = self.request.POST['moeda']

        data_inicial = datetime.strptime(
            self.request.POST['data_inicial'], '%Y-%m-%d').date()
        data_final = datetime.strptime(
            self.request.POST['data_final'], '%Y-%m-%d').date()

        CotacaoMoedas(moeda, data_inicial, data_final).atualizar_banco()

        response['HX-Trigger'] = 'hx-list-updated'
        messages.success(self.request, 'Cotação concluída!')
        return response


class CotacaoHtmxListView(ListView):
    model = Cotacao
    template_name = 'core/partials/htmx_cotacao_list.html'
    context_object_name = 'cotacoes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not Cotacao.objects.filter(data_inicial=datetime.now().date()):
            moeda = retornar_moeda()
            data_final = datetime.now().date()
            data_inicial = data_final - timedelta(days=4)
            while verifica_dia_util(data_inicial) == False:
                data_inicial = data_inicial - timedelta(days=1)

            CotacaoMoedas(moeda, data_inicial, data_final).atualizar_banco()

        context['moeda'] = json.dumps(retornar_moeda())
        context['valores_moeda'] = json.dumps(retornar_valores_grafico())
        context['dia_inicial'] = json.dumps(retornar_data_inicial(self))
        context["cotacoes"] = Cotacao.objects.all().order_by('-id')
        return context


class CotacaoHtmxDeleteView(SuccessMessageMixin, DeleteView):
    model = Cotacao
    success_message = 'Cotação excluída!'
    template_name = 'core/partials/htmx_cotacao_list.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        cotacoes = Cotacao.objects.filter(
            id=self.object.id)
        self.object.delete()
        cotacoes = Cotacao.objects.all().order_by('-id')
        messages.success(request, self.success_message)
        return render(request, self.template_name, {'cotacoes': cotacoes})
