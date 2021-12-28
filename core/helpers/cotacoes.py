import requests
from core.models import Cotacao
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.db.models import Q


class CotacaoMoedas():

    def __init__(self, moeda: str, data: datetime):
        self.moeda = moeda
        self.data = data
        self.valor = 0

    def obter_cotacao(self):
        # Função para obter a cotação conforme a data e moeda escolhida
        # Consumindo a API api.vatcomply.com
        if self.verifica_dia_util():
            data = self.data.strftime('%Y-%m-%d')
            url = "https://api.vatcomply.com/rates?date=" + data + "&base=USD"
            retorno = requests.get(url)
            if (retorno.status_code == 200):
                json = retorno.json()
                self.valor = json['rates'][self.moeda]
            else:
                self.valor = 0
            return self.valor

    def verifica_dia_util(self):
        # Verifica se a data é um dia útil antes de obter a cotação.
        if self.data.weekday() < 5:
            return True

    def atualizar_banco(self):
        # Chama o método da classe para obter a cotação e gravar no BD.
        self.obter_cotacao()
        Cotacao.objects.create(valor=float(self.valor),
                               data_inicial=self.data, moeda=self.moeda)
