import requests
from core.models import Cotacao
from datetime import datetime
from django.http import JsonResponse


class CotacaoMoedas():

    def __init__(self, moeda: str, data: str):
        self.moeda = moeda
        self.data = data
        self.valor = 0

    def obter_cotacao(self):
        # https://api.vatcomply.com/rates?base=USD
        # https://api.vatcomply.com/rates?date=2000-04-05&base=USD
        # url = "https://economia.awesomeapi.com.br/last/" + self.moeda + "-BRL"
        url = "https://api.vatcomply.com/rates?date=" + self.data + "&base=USD"
        retorno = requests.get(url)
        if (retorno.status_code == 200):
            json = retorno.json()
            self.valor = json[self.moeda]
        else:
            self.valor = 0
        return self.valor

    def atualizar_banco(self):
        self.obter_cotacao()
        Cotacao.objects.filter(moeda=self.moeda).update(
            valor=float(self.valor),
            data=datetime.today()
        )
