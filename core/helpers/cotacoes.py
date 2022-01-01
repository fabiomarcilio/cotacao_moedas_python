import requests
from core.models import Cotacao
from datetime import datetime, timedelta
from core.helpers.funcoes import verifica_dia_util


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

    def atualizar_banco(self):
        # Chama o método da classe para obter a cotação e gravar no BD.
        data_inicio_base = self.data_inicial
        while self.data_inicial <= self.data_final:
            if verifica_dia_util(self.data_inicial):
                self.obter_cotacao()
                Cotacao.objects.create(valor=float(self.valor),
                                       data_inicial=data_inicio_base,
                                       data_final=self.data_final,
                                       data_cotacao=self.data_inicial,
                                       moeda=self.moeda,
                                       status='Consulta ok')
                self.data_inicial += timedelta(days=1)
            else:
                Cotacao.objects.create(valor=0,
                                       data_inicial=data_inicio_base,
                                       data_final=self.data_final,
                                       data_cotacao=self.data_inicial,
                                       moeda=self.moeda,
                                       status='Dia não útil')
                self.data_inicial += timedelta(days=1)
                if self.data_final < datetime.now().date():
                    self.data_final += timedelta(days=1)
