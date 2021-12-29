from django.urls import path

from .views import SiteTemplateview, CotacaoHtmxCreateView, CotacaoHtmxListView, CotacaoHtmxDeleteView

app_name = 'core'

urlpatterns = [
    path(
        route='',
        view=SiteTemplateview.as_view(),
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
    path(
        route='<int:pk>/delete/',
        view=CotacaoHtmxDeleteView.as_view(),
        name='delete'
    ),
]
