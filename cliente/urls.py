from django.urls import path
from .views import *
from .models import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    # Página Principal
    path('Inicio', pagina_principal, name='pagina_principal'),  

    #Clientes
    path('cliente/inserir_cliente', inserir_clientes, name='inserir_clientes'),  
    path('cliente/listar_cliente', listar_clientes, name='listar_clientes'),  
    path('cliente/editar_cliente/<str:id>', editar_clientes, name='editar_clientes'),  
    path('cliente/editar_cliente2/<str:id>', editar_clientes2, name='editar_clientes2'),  
    path('cliente/remover_cliente/<str:id>', remover_clientes, name='remover_clientes'),  
    

    #Factorings
    path('cliente/inserir_factoring', inserir_factorings, name='inserir_factorings'),
    path('cliente/listar_factoring', listar_factorings, name='listar_factorings'),
    path('cliente/editar_factoring/<str:id>', editar_factorings, name='editar_factorings'),
    path('cliente/editar_factoring2/<str:id>', editar_factorings2, name='editar_factorings2'),
    path('cliente/remover_factoring/<str:id>', remover_factorings, name='remover_factorings'),

    #Pessoas
    path('cliente/inserir_pessoa', inserir_pessoas, name='inserir_pessoas'),
    path('cliente/listar_pessoa', listar_pessoas, name='listar_pessoas'),
    path('cliente/editar_pessoa/<str:id>', editar_pessoas, name='editar_pessoas'),
    path('cliente/editar_pessoa2/<str:id>', editar_pessoas2, name='editar_pessoas2'),
    path('cliente/remover_pessoa/<str:id>', remover_pessoas, name='remover_pessoas'),    

    #Contrato Mãe
    path('cliente/inserir_contratomae', inserir_contratomae, name='inserir_contratomae'),
    path('cliente/listar_contratomae', listar_contratomae, name='listar_contratomae'),
    path('gerar_contrato_word/<int:cma_id>/', gerar_contrato_word, name='gerar_contrato_word'),
    path('cliente/editar_contratomae2/<str:id>', editar_contratomae2, name='editar_contratomae2'),

    #Simulação
    path('cliente/inserir_simulacao', inserir_simulacao, name='inserir_simulacao'),    
    path('cliente/listar_simulacaoid/<str:id>', listar_simulacaoid, name='listar_simulacaoid'),
    path('gerar_simulacao_word/<int:sim_id>/', gerar_simulacao_word, name='gerar_simulacao_word'),
    path('cliente/listar_simulacao', listar_simulacao, name='listar_simulacao'),
    path('cliente/listar_simulacaocopy', listar_simulacaocopy, name='listar_simulacaocopy'),
    path('cliente/editar_simulacao2/<str:id>', editar_simulacao2, name='editar_simulacao2'),
    
    #Simulação
    path('cliente/inserir_operacao/<int:id>/', inserir_operacao, name='inserir_operacao'),
    path('cliente/listar_operacao', listar_operacao, name='listar_operacao'),
    path('gerar_operacao_word/<int:ope_id>/', gerar_operacao_word, name='gerar_operacao_word'),
    path('cliente/listar_operacaoid/<str:id>', listar_operacaoid, name='listar_operacaoid'),
    path('cliente/editar_operacao/<str:id>', editar_operacao, name='editar_operacao'),
]