from django import forms

from core.models import Cotacao

from core.models import MOEDAS


class CotacaoModelForm(forms.ModelForm):

    class Meta:
        model = Cotacao
        fields = ['moeda', 'data_inicial', 'data_final', 'valor']

    moeda = forms.ChoiceField(required=True, label='Moeda', choices=MOEDAS, widget=forms.Select(
        attrs={'class': 'form-control'}), initial='BRL')
    data_inicial = forms.CharField(label='Data Inicial', widget=forms.DateInput(
        format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}))
    data_final = forms.CharField(label='Data Final', widget=forms.DateInput(
        format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}))
    # valor = forms.CharField(label='Valor', widget=forms.TextInput(
    #     attrs={'class': 'form-control'}))
