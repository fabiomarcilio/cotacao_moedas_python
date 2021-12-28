from django.db import models

MOEDAS = [
    # ('USD', 'Dolar'),
    ('BRL', 'Real'),
    ('EUR', 'Euro'),
    ('JPY', 'Iene'),
]


# class Moedas(models.Model):

#     moeda = models.CharField(
#         max_length=15, blank=False, null=False, choices=MOEDAS, default='BRL')

#     class Meta:
#         db_table = 'moedas'
#         verbose_name = 'Moeda'
#         verbose_name_plural = 'Moedas'


class Cotacao(models.Model):

    # moeda = models.ForeignKey(
    #     Moedas, related_name='moedas', blank=True, null=True, on_delete=models.PROTECT)
    moeda = models.CharField(
        max_length=15, blank=False, null=False, choices=MOEDAS, default='BRL')
    data_inicial = models.DateField(blank=True, null=True)
    data_final = models.DateField(blank=True, null=True)
    valor = models.DecimalField(
        max_digits=10, decimal_places=6, default=0, blank=False, null=False)

    class Meta:
        db_table = 'cotacoes'
        verbose_name = 'Cotações'
        verbose_name_plural = 'Cotacoes'
