import requests
from core.models import Cotacao
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.db.models import Q


class CotacaoMoedas():

    def __init__(self, moeda: str, data_inicial: datetime, data_final: datetime):
        self.moeda = moeda
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.valor = 0

    def obter_cotacao(self):
        # Função para obter a cotação conforme a data e moeda escolhida
        # Consumindo a API api.vatcomply.com
        data = self.data_inicial.strftime('%Y-%m-%d')
        url = "https://api.vatcomply.com/rates?date=" + data + "&base=USD"
        retorno = requests.get(url)
        if (retorno.status_code == 200):
            json = retorno.json()
            self.valor = json['rates'][self.moeda]
        else:
            self.valor = 0
        return self.valor

    def verifica_dia_util(self, data):
        # Verifica se a data é um dia útil antes de obter a cotação.
        if data.weekday() < 5:
            return True

    def atualizar_banco(self):
        # Chama o método da classe para obter a cotação e gravar no BD.
        while self.data_inicial <= self.data_final:
            if self.verifica_dia_util(self.data_inicial):
                self.obter_cotacao()
                Cotacao.objects.create(valor=float(self.valor),
                                       data_inicial=self.data_inicial, data_final=self.data_final, moeda=self.moeda, status='Consulta ok')
                self.data_inicial += timedelta(days=1)
            else:
                self.data_inicial += timedelta(days=1)
                self.data_final += timedelta(days=1)
