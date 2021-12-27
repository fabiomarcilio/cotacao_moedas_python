from django.urls import path

from .views import site, CotacaoHtmxCreateView, CotacaoHtmxListView

app_name = 'core'

urlpatterns = [
    path(
        route='',
        view=site,
        name='index',
    ),
    path(
        route='create',
        view=CotacaoHtmxCreateView.as_view(),
        name='create',
    ),
    path(
        route='list',
        view=CotacaoHtmxListView.as_view(),
        name='list',
    ),
    # path(
    #     route='atualizar_valor_indexador/',
    #     view=atualizar_valor_indexador,
    #     name='atualizar_valor_indexador'
    # ),
]
