from datetime import datetime, timedelta
from core.models import Cotacao


def retornar_valores_grafico(self):
    data = []
    cotacoes = Cotacao.objects.filter(moeda=retornar_moeda(self))[:5]
    for cotacao in cotacoes:
        data.append(float(cotacao.valor))
    return data


def retornar_moeda(self):
    moeda = Cotacao.objects.filter().last().moeda
    return moeda


def retornar_data_inicial(self):
    data = Cotacao.objects.filter(
        moeda=retornar_moeda(self)).first().data_inicial.day
    # if self.request.POST.get('data_inicial'):
    #     data = self.request.POST.get('data_inicial')
    # else:
    #     data_inicial = datetime.now() - timedelta(days=5)
    #     data = data_inicial.day
    return data
