from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('advogados/', views.lista_advogados, name='lista_advogados'),
    path('advogados/novo/', views.criar_advogado, name='criar_advogado'),
    path('advogados/<int:pk>/editar/', views.editar_advogado, name='editar_advogado'),
    path('advogados/<int:pk>/excluir/', views.excluir_advogado, name='excluir_advogado'),

    path('casos/', views.lista_casos, name='lista_casos'),
    path('casos/novo/', views.criar_caso, name='criar_caso'),
    path('casos/<int:pk>/editar/', views.editar_caso, name='editar_caso'),
    path('casos/<int:pk>/excluir/', views.excluir_caso, name='excluir_caso'),
]
