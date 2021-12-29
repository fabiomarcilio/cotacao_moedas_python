from datetime import datetime, timedelta
from core.models import Cotacao


def retornar_valores_grafico(self):
    data = []
    # data_final = datetime.now().date()
    # data_inicial = data_final - timedelta(days=4)
    cotacoes = Cotacao.objects.filter(moeda='BRL')
    for cotacao in cotacoes:
        data.append(float(cotacao.valor))
    return data


def retornar_moeda(self):
    teste = ''
    if self.request.POST.get('moeda'):
        moeda = self.request.POST.get('moeda')
    else:
        moeda = 'BRL'
    return moeda


def retornar_data_inicial(self):
    if self.request.POST.get('data_inicial'):
        data = self.request.POST.get('data_inicial')
    else:
        data_inicial = datetime.now() - timedelta(days=5)
        data = data_inicial.day
    return data
