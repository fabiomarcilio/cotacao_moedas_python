from datetime import datetime, timedelta
from core.models import Cotacao


def verifica_dia_util(data: datetime):
    # Verifica se a data é um dia útil antes de obter a cotação.
    if data.weekday() < 5:
        return True
    else:
        return False


def retorna_valores_grafico():
    # Retorna os valores em uma lista para popular o gráfico.
    data = []
    cotacoes = Cotacao.objects.filter(moeda=retorna_moeda())[:5]
    for cotacao in cotacoes:
        data.append(float(cotacao.valor))
    return data


def retorna_moeda():
    # Retorna a sigla da moeda
    if Cotacao.objects.all().exists():
        moeda = Cotacao.objects.filter().last().moeda
    else:
        moeda = 'BRL'
    return moeda


def retorna_data_inicial(self):
    # Calcula a data inicial considerando a data final.
    if self.request.POST.get('data_inicial'):
        data = self.request.POST.get('data_inicial')
    else:
        if Cotacao.objects.all().exists():
            data = Cotacao.objects.filter(
                moeda=retorna_moeda()).last().data_inicial
        else:
            data_final = datetime.now().date()
            data_inicial = data_final - timedelta(days=4)
            while verifica_dia_util(data_inicial) == False:
                data_inicial = data_inicial - timedelta(days=1)
            data = data_inicial
    return data


def retorna_dias_grafico(self):
    # Retorna uma lista de string dos dias das cotações,
    # desconsiderando os finais de semana.
    dias = []
    data_inicial = retorna_data_inicial(self)
    data_final = data_inicial + timedelta(days=4)
    hoje = datetime.now().date()

    while data_final > hoje:
        data_final = data_final - timedelta(days=1)
        data_inicial = data_inicial - timedelta(days=1)

    while data_inicial <= data_final:
        if verifica_dia_util(data_inicial) == True:
            dias.append(str(data_inicial.day))
            data_inicial = data_inicial + timedelta(days=1)
        else:
            data_inicial = data_inicial + timedelta(days=1)
            if data_final <= hoje:
                data_final = data_final + timedelta(days=1)

    return dias
