from datetime import datetime, timedelta
from core.models import Cotacao


def verifica_dia_util(data: datetime):
    # Verifica se a data é um dia útil antes de obter a cotação.
    if data.weekday() < 5:
        return True
    else:
        return False


def retornar_valores_grafico():
    # Retorna os valores em uma lista para popular o gráfico.
    data = []
    cotacoes = Cotacao.objects.filter(moeda=retornar_moeda())[:5]
    for cotacao in cotacoes:
        data.append(float(cotacao.valor))
    return data


def retornar_moeda():
    teste = ''
    # Retorna a sigla da moeda
    if Cotacao.objects.all().exists():
        moeda = Cotacao.objects.filter().last().moeda
    else:
        moeda = 'BRL'
    return moeda


def retornar_data_inicial(self):
    # Calcula a data inicial considerando a data final.
    if self.request.POST.get('data_inicial'):
        data = self.request.POST.get('data_inicial')
    else:
        if Cotacao.objects.all().exists():
            data = Cotacao.objects.filter(
                moeda=retornar_moeda()).first().data_inicial.day
        else:
            data_final = datetime.now().date()
            data_inicial = data_final - timedelta(days=4)
            while verifica_dia_util(data_inicial) == False:
                data_inicial = data_inicial - timedelta(days=1)
            data = data_inicial.day
    return data
